from optparse import OptionGroup, OptionParser
from urllib2 import Request, URLError, urlopen
import base64
import codecs
import cStringIO
import csv
import hashlib
import hmac
import httplib
import json
import os
import re
import string
import sys
import urllib
import MySQLdb

date_regex = r'^[0-9][0-9][0-9][0-9]-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])( ([01][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)?$'
client_id_regex = r'^c[a-z0-9]{24}$'
signing_key_regex = r'^[-_a-zA-Z0-9]{43}$'


def url_sign( uri_path, params, client_id, signing_key ):
    signing_key = signing_key.translate(string.maketrans('-_', '+/'))
    padding_factor = ( 4 - len( signing_key ) % 4 ) % 4
    signing_key += "=" * padding_factor
    binary_key = base64.b64decode(unicode(signing_key).translate(dict(zip(map(ord, u'-_'), u'+/'))))

    # construct URI for signing
    uri_path_params = uri_path + '?'
    first = True
    for k in params.keys():
        if not first:
            uri_path_params += '&'
        else:
            first = False
        uri_path_params = "%(base)s%(key)s=%(value)s" % {
                                                        'base':uri_path_params,
                                                        'key':k,
                                                        'value':urllib.quote_plus(str(params[k]))
                                                        }
    uri_path_params += '&client=' + client_id

    # Sign
    digest = hmac.new(binary_key, uri_path_params, hashlib.sha1).digest()
    digest = base64.b64encode( digest )
    digest = digest.translate(string.maketrans('+/', '-_'))
    return "%s&sig=%s" % ( uri_path_params, digest.rstrip('=') )


def get_data(url):
    try:
        headers = {'Accept':'application/json'}
        request = Request(url, headers=headers)
        conn = urlopen(request)
        if int(conn.code) != httplib.OK:
            sys.stderr.write("Error getting data. Some data may already have been retrieved.\n")
            sys.stderr.write("Response data: %(data)s\n" % {'data':conn.read()})
            sys.exit(2)
        response = conn.read()
    except URLError, e:
        sys.stderr.write("Error getting data. Some data may already have been retrieved.\n")
        sys.stderr.write("%(error)s\n" % {'error':str(e)})
        sys.stderr.write("Response data: %(data)s\n" % {'data':e.read()})
        sys.exit(2)

    return json.loads(response)


class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    This is from the python documentation on the csv library.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        try:
            result = []
            for s in row:
                if s == None:
                    result.append("")
                elif s.__class__ is not u''.__class__:
                    result.append(str(s))
                else:
                    try:
                        result.append(s.encode("utf-8"))
                    except UnicodeEncodeError:
                        pass

            self.writer.writerow(result)
            
            # Fetch UTF-8 output from the queue ...
            data = self.queue.getvalue()
            data = data.decode("utf-8")
            # ... and reencode it into the target encoding
            data = self.encoder.encode(data)
            # write to the target stream
            self.stream.write(data)
            # empty queue
            self.queue.truncate(0)
        except Exception as e:
            print e
            pass
            

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


def output_csv_header_line(outfile, linked_status):
    writer = UnicodeWriter(outfile)
    if linked_status:
        writer.writerow([
                         'location_id',
                         'name',
                         'address1',
                         'address2',
                         'city',
                         'region',
                         'postcode',
                         'country',
                         'latitude',
                         'longitude',
                         'phone',
                         'linked_status',
                         'businessType',
                         'outOfBusiness',
                         'publishedAt',
                         ])
    else:
        writer.writerow([
                         'location_id',
                         'name',
                         'address1',
                         'address2',
                         'city',
                         'region',
                         'postcode',
                         'country',
                         'latitude',
                         'longitude',
                         'phone',
                         'businessType',
                         'outOfBusiness',
                         'publishedAt',
                         ])

#def output_mysql(data):
    
    

def output_csv(data, location_ids, outfile, linked_status):
    writer = UnicodeWriter(outfile)
    for record in data:
        if record['id'] in location_ids:
            continue
        location_ids.add(record['id'])
        if linked_status:
            row = [
                record['id'],
                record['general']['name'],
                record['location']['address1'],
                record['location']['address2'],
                record['location']['city'],
                record['location']['region'],
                record['location']['postcode'],
                record['location']['country'],
                record['location']['latitude'],
                record['location']['longitude'],
                record['phones']['main'],
                record.get('isOwnerVerified', 'false')
                ]
        else:
            row = [
                record['id'],
                record['general']['name'],
                record['location']['address1'],
                record['location']['address2'],
                record['location']['city'],
                record['location']['region'],
                record['location']['postcode'],
                record['location']['country'],
                record['location']['latitude'],
                record['location']['longitude'],
                record['phones']['main'],
                ]
        if 'businessType' in record:
            row.append(record['businessType'])
        else:
            row.append('')

        if record['outOfBusiness']:
            row.append('t')
        else:
            row.append('f')

        row.append(record['publishedAt'])

        writer.writerow(row)


def load_updated_locations(options):
    keep_going = True
    params = {
        'page': -1,
        'q': options.query,
        'count': options.page_size,
        'updatedSince': options.updated_since,
    }
    new_updated_since = None
    output_location_ids = set()
    output_csv_header_line(options.outfile, options.linked_status)
    while keep_going:
        # get URL for this page of results
        params['page'] += 1
        uri_path_and_query = url_sign('/restaurants/search',
                                      params,
                                      options.client_id,
                                      options.signing_key)
        url = 'http://%(hostname)s%(path_and_query)s' % {
                                                        'hostname':options.hostname,
                                                        'path_and_query':uri_path_and_query
                                                        }

        # Make request for data
        response = get_data(url)

        # Remember the query time for the first query as the value to use for next time
        if 0 == params['page']:
            new_updated_since = response['time']

        # Output the data
        output_csv(response['results'], output_location_ids, options.outfile, options.linked_status)
        
        ## Ouput the data To MySQL
        #output_mysql(response['results'])
        

        # Are we done yet?
        if int(response['count']) < int(params['count']):
            params['count'] = response['count']

        total_pages = int(response['total']) / int(response['count'])
        if total_pages < response['page']:
            keep_going = False

        if options.verbose:
            sys.stderr.write(url + "\n")


    sys.stderr.write("date/time to use for next run: %(next_time)s\n"
                     % {'next_time': new_updated_since})
    sys.stderr.write("number locations changed: %(changed)s\n" % {'changed':len(output_location_ids)})


def get_options_parser():
    description = "This program downloads all locations updated since X date into a CSV file."
    usage = "Usage: %prog [options]"
    version = "%prog 1.0"
    parser = OptionParser(description=description, usage=usage, version=version)

    group = OptionGroup(parser, "Required")
    group.add_option("-c", "--client-id", default=False,
        help="The client ID to use in making the calls",
        action="store", dest="client_id", metavar="CLIENT_ID")

    group.add_option("-s", "--signing_key", default=False,
        help="The signing key to use in making the calls",
        action="store", dest="signing_key", metavar="SIGNING_KEY")

    group.add_option("-u", "--updated-since", default=False,
        help="The date/time after which you want updated locations. The format is \"YEAR-MONTH-DAY HOUR:MINUTE:SECOND\", the hours are in 24 hour time and the date/time is in Eastern Standard Time (EST). Examples: \"2012-01-05\", \"2012-01-05 22:55\", \"2012-01-05 22:55:04\"",
        action="store", dest="updated_since", metavar="UPDATED_SINCE")
 
    parser.add_option_group(group)

    group = OptionGroup(parser, "Optional")
    group.add_option("-q", "--query", default='',
        help="A query by which to filter the results",
        action="store", dest="query", metavar="QUERY")

    group.add_option("-o", "--out", default=False,
        help="The path to an output file (defaults to using stdout)",
        action="store", dest="outfile", metavar="OUTFILE")
 
    group.add_option("-H", "--hostname", default="api.singleplatform.co",
    #    group.add_option("-H", "--hostname", default="api.qa.menuplatform.net",
        help="Specify hostname to deploy to (default: api.singleplatform.co)",
        action="store", dest="hostname", metavar="HOSTNAME")

    group.add_option("-p", "--page-size", default=3000,
        help="The number of locations to return for each query to the server. (Multiple queries are often required to download all the data.) (default: 3000)",
        action="store", dest="page_size", metavar="PAGE_SIZE")

    group.add_option("-v", "--verbose", 
        help="Print extra information about what is happening to stderr",
        action="store_true", dest="verbose")

    group.add_option("-l", "--linked-status",
        help="Show whether or not linked to a business",
        action="store_true", dest="linked_status", metavar="LINKED_STATUS")

    parser.add_option_group(group)

    return parser


def validate_options(options):
    if not options.client_id:
        sys.stderr.write("Client ID is required\n")
        sys.exit(1)

    if not re.match(client_id_regex, options.client_id):
        sys.stderr.write("Invalid client ID\n")
        sys.exit(1)

    if not options.signing_key:
        sys.stderr.write("Signing key is required\n")
        sys.exit(1)

    if not re.match(signing_key_regex, options.signing_key):
        sys.stderr.write("Invalid signing_key\n")
        sys.exit(1)

    if not options.updated_since:
        sys.stderr.write("Updated since date/time is required\n")
        sys.exit(1)

    if not re.match(date_regex, options.updated_since):
        sys.stderr.write("Invalid date/time for updated since\n")
        sys.exit(1)

    try:
        options.page_size = int(options.page_size)
    except ValueError, e:
        sys.stderr.write("Invalid page size. It must be an integer.\n")
        sys.exit(1)

    if not options.outfile:
        if "win32" == sys.platform:
            import msvcrt
            msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
        options.outfile = sys.stdout
    else:
        try:
            options.outfile = open(options.outfile, 'wb')
        except IOError, e:
            print "Error opening file '%(filename)s': %(message)s" % \
                    {'message':e.strerror, 'filename':e.filename}
            sys.exit(1)


def main():
    parser = get_options_parser()
    (options, args) = parser.parse_args()
    validate_options(options)

    load_updated_locations(options)


if __name__ == "__main__":
    main()

