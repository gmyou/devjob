#log2json.py
import datetime
import re


logDate = '20120824'

#log = '/data/logs/localhost_access_log.'+logDate+'.log'
log = '/data/logs/read1/localhost_access_log.'+logDate+'.log'

s = datetime.datetime.now()
print("Start : "+str(s))

f = open(log)
w = file('uuid', 'w')



def extractUrl(fullUrl):
	arr = fullUrl.split('.jsp?')
	url = arr[0]
	url = url.replace('/galaxy/xml/', '')

	print logDate
	print '\t', url
	#TODO colletioin

	param =  arr[1]
	arrParam = param.split('&')

	for i, p in enumerate(arrParam):
		print '\t', '\t', i, p
		#TODO document



for line in f:
	#print "line.find('uuid=')", line.find('uuid=')
	if ( line.find('uuid=')>-1 ):
	    arr1 = line.split(' ')
	    #print "line.find('appidx=')", line.find('uuid=')
	    for i, a in enumerate(arr1):
	    	if ( a.find('appidx=')>-1 ):
	    		extractUrl(a)


	    
f.close()
w.close()


e = datetime.datetime.now()
print("End : "+str(e))