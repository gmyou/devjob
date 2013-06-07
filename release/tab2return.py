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
        if ( line.find('\t')>-1 ):
                arr = line.split('\t')
		for ip in arr:
			if ( bool(re.match('[0-9]', ip[:1])) ):
				#print(ip)
				w.write(ip)
				w.write('\n')
				i += 1
        elif ( line.find('\t')>-1 ):
		if ( bool(re.match('[0-9]', line[:1])) ):
			print(line)
			w.write(line)
			w.write('\n')

f.close()
w.close()

e = datetime.datetime.now()
print("End : "+str(e))

print("Total. "+ str(i))
