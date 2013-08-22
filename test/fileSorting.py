#!/usr/bin/env python3.3

import os

term = "food"

#path = "./"+term+"/ca/"
path = "./"+term+"/ca/"
dirList = os.listdir(path)

fnumList = {}
fsize_tmp = 0

for fname in dirList:
    if (fname.endswith(".json")):
        fsize = os.path.getsize(path+fname)
        fnum = fname.replace(term+"_ca_", "")
        fnum = fnum.replace(".json", "")
        #if (fsize>271):
        if (fsize>271 and int(fnum)<1806):
            fnumList[int(fnum)] = fsize        


for key in sorted(fnumList.iterkeys()):
    if (fsize_tmp != fnumList[key]):
        print key, fnumList[key]
    fsize_tmp = fnumList[key]

