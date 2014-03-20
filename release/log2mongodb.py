#log2json.py
import datetime
import re
import json
import types
from pymongo import MongoClient

logDate = '20120824'
#log = '/data/logs/read1/localhost_access_log.20120824.log'
log = '/data/logs/localhost_access_log.'+logDate+'.log'

s = datetime.datetime.now()
print("Start : "+str(s))

f = open(log)
w = file('uuid', 'w')

client = MongoClient('localhost', 27017)
db = client.weblog

def extractUrl(fullUrl):

	global db

	arr = fullUrl.split('.jsp?')
	url = arr[0]
	url = url.replace('/galaxy/xml/', '')

	print url
	

	strJson = '{"date":"'+logDate+'",'
	strJson += '"url":"'+url+'",'

	param =  arr[1]
	arrParam = param.split('&')

	
	for i, p in enumerate(arrParam):
		print '\t', i, p
		arrP = p.split('=')
		
		strJson += '"'+arrP[0]+'":"'+arrP[1]+'",'
	
	if ( strJson.endswith(',') ):
		strJson = strJson[:-1]

	strJson += '}'
	print strJson
	j = json.loads(strJson)
	insertData(j)
		
def insertData(data):
	collection = db.dummy
	collection.insert(data)


try:

	for line in f:
		#print "line.find('uuid=')", line.find('uuid=')
		if ( line.find('uuid=')>-1 ):
		    arr1 = line.split(' ')
		    #print "line.find('appidx=')", line.find('uuid=')
		    for i, a in enumerate(arr1):
		    	if ( a.find('appidx=')>-1 ):
		    		extractUrl(a)

finally:
    
	f.close()
	w.close()
	#db connection close

e = datetime.datetime.now()
print("End : "+str(e))