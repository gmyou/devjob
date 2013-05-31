import datetime

s = datetime.datetime.now()
print("Start : "+str(s))

f = open('/data/localhost_access_log.20121024_stats.log')
w = file('ip', 'w')
i = 0

for line in f:
        arr = line.split()
        w.write(arr[0])
        w.write('\n')
        i += 1

f.close()
w.close()

e = datetime.datetime.now()
print("End : "+str(e))


print("Total. "+ str(i))
