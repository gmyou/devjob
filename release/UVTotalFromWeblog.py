import datetime

#Start Time Display

s = datetime.datetime.now()
print("Start : "+str(s))

f = open('localhost_access_log.20121024_stats.log')
w = file('ip', 'w')
i = 0
j = 0

for line in f:
        arr = line.split()
        w.write(arr[0])
        w.write('\n')
        i += 1

f.close()



w.close()



#Read IP and Distinct

with open('ip') as f:
    lines = f.read().splitlines()

uv = list(set(lines))

u = file('ip_unique', 'w')

for line in uv:
        u.write(line)
        u.write('\n')
        j += 1


#End Time Diplay
e = datetime.datetime.now()
print("End : "+str(e))

print("Total. " + str(i))
print("UV. " + str(j))
