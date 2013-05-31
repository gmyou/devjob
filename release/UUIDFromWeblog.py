import datetime

s = datetime.datetime.now()
print("Start : "+str(s))

f = open('localhost_access_log.20121024_stats.log')
w = file('uuid', 'w')
i = 0

for line in f:
        if line.find('uuid=')>-1:
                arr = line.split('uuid=')
                uuid = arr[1][:36]
                w.write(uuid)
                w.write('\n')
                i += 1

f.close()
w.close()

e = datetime.datetime.now()
print("End : "+str(e))

print("Total. "+ str(i))
