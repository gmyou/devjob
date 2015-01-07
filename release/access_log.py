line = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] "GET / HTTP/1.1" 401 401 "" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827"'
regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"'

import re

# Test
print re.match(regex, line).groups()


f = open('./logs/access.log')
# print (f.read())
i = 0

referer = {}

for l in f:
	i+=1
	try:
		log = re.match(regex, l).groups()
		# print i, log[0], log[3], log[6]
		# print referer.has_key(log[6])

		if (referer.has_key(log[6])):
			referer[log[6]] += 1
		else:
			referer[log[6]] = 1

	except Exception, e:
		print e
	finally:
		pass
		# print l
		

print referer
import operator
		
sorted_x = sorted(referer.items(), key=operator.itemgetter(1))
for ref in sorted_x:
	print ref[1], ref[0]
