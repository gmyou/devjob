#log2mongodb.py

import datetime
import re
import sys
import json
import types
from pymongo import MongoClient

logDate = '2015-04-17'

# log = '/data/logs/localhost_access_log.'+logDate+'.log'
#log = '/data/logs/read1/localhost_access_log.'+logDate+'.log'
#log = '/data/logs/read2/localhost_access_log.'+logDate+'.log'
#log = '/data/logs/read3/localhost_access_log.'+logDate+'.log'
# localhost_access_log.2015-04-17.txt
log = 'd:/data/logs/localhost_access_log.'+logDate+'.txt'

s = datetime.datetime.now()
print("Start : "+str(s))

f = open(log)
w = file('log2mongodb.py.log', 'a')
client = MongoClient('localhost', 27017)
db = client.webLog

def extractUrl(fullUrl):

	global db
	print fullUrl

	ip = fullUrl[0]
	code = fullUrl[8]
	url = fullUrl[6]

	print url

	strJson = '{"date":"'+logDate+'"'
	strJson += ',"ip":"'+ip+'"'
	strJson += ',"code":"'+code+'"'
	strJson += ',"url":"'+url+'"'
	strJson += '}'
	print strJson
	j = json.loads(strJson)
	print j
	insertData(j)
		
def insertData(data):
	collection = db.dummy
	collection.insert(data)


try:

	for line in f:
		print line

		
		if ( line.find('http://10.33.209.243')>-1 ):
		    arr1 = line.split(' ')
		    extractUrl(arr1)
		    w.write("[Insert] "+str(arr1)+"\n")

except:
	w.write("[Error] "+str(sys.exc_info()[0])+"\n")

finally:
    
	f.close()
	w.close()
	#db connection close

e = datetime.datetime.now()
print("End : "+str(e))
