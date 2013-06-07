import datetime
import re

#ip = "10.*"
#print ip[:1]
#print bool(re.match(ip[:1], '1'))
#print bool(re.match('[0-9]*th', '35th'))
#print bool(re.match('[0-9]', ip))

s = datetime.datetime.now()
print("Start : "+str(s))

f = open('ir_ips.txt')
w = file('ir_ips_line.txt', 'w')
i = 0

for line in f:
        arr = re.split(r"[\t,\n,\r]", line)
	for ip in arr:
		if ( bool(re.match('[0-9]', ip[:1])) ):
			w.write(ip)
			w.write('\n')
			i += 1

f.close()
w.close()

e = datetime.datetime.now()
print("End : "+str(e))

print("Total. "+ str(i))
