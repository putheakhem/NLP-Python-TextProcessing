#!/usr/bin/env python

"""Merge File into Single File"""

__author__      = "Khem Puthea"
__copyright__   = "Copyright 2021, puthea.khem@gmail.com"

import sys
data = data2 = "" 
count = 0

print(sys.argv[-1])
print(sys.argv[-2])
print(sys.argv[-3])
firstFile = sys.argv[-3]
secondFile = sys.argv[-2]
mergedFile = sys.argv[-1]

with open(firstFile, "r", encoding='utf-8') as fp:      
    data = fp.read() 
  
# Reading data from file2 
with open(secondFile, "r", encoding='utf-8') as fp: 
    data2 = fp.read() 
data +="\n"
data += data2 

with open(mergedFile, 'a+', encoding='utf-8') as fp: 
    fp.write(data) 