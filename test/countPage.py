import datetime

s = datetime.datetime.now()
print("Start : "+str(s))


############################ weblog 2 url
#f = open("c:/temp/20120911_web.log", 'r')

#w = file('c:/temp/url', 'w')


#for line in f:
    #arr = line.split()
    #w.write(arr[6])
    #w.write('\n')

#f.close()
#w.close()


############################ url 2 page

page = {'nation_check':1}
#print(page.keys())

def countPage(pageName):
    gubun = "/stats/xml/"
        
    
    if pageName.find(gubun)>-1:    
        global page    
        arr = pageName.split(gubun)
        pageName = arr[1]
        
        if pageName in page.keys():
            count = page[pageName]
            count += 1          
            page[pageName]=count
        else:
            page[pageName]=1


for line in open("c:/temp/url", 'r'):
    if line.find('.jsp?')>-1:
        arr = line.split(".jsp?")
        countPage(arr[0])
         
        
print(page)


#import pymongo
#connection = pymongo.Connection("192.168.175.132", 27017)
#db = connection.weblog
#db.weblog

#while 1:
        #line = f.readline()
        #if not line: break
        #db.weblog.raw_daily.save({"regdate":"20120425", "raw":line})
        #print(line)

#f.close()



e = datetime.datetime.now()
print("End : "+str(e))
