import datetime
import time
import re

#ip = "10.*"
#print ip[:1]
#print bool(re.match(ip[:1], '1'))
#print bool(re.match('[0-9]*th', '35th'))
#print bool(re.match('[0-9]', ip))

s = datetime.datetime.now()
print("Start : "+str(s))

f = open('/data/ir_ips.txt')
w = file('/data/ir_ips_line.txt', 'w')
i = 0

for line in f:
        arr = re.split(r"[\t,\n,\n]", line)
	for ip in arr:
		if ( bool(re.match(r'[0-9]', ip[:1])) ):
			print(str(i)+"\t"+ip)
			w.write(ip)
			w.write('\n')
			i += 1
			time.sleep(0.1)

f.close()
w.close()

e = datetime.datetime.now()
print("End : "+str(e))

print("Total. "+ str(i))
