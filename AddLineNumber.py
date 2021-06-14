#!/usr/bin/env python

"""Adding Line Number To Every Sentences"""

__author__      = "Khem Puthea"
__copyright__   = "Copyright 2021, puthea.khem@gmail.com"

import sys
filename = sys.argv[-1]

original = open(filename, 'r')
addLine = open('WithLineNumber' +filename + '', 'w')

count = 000000
while True:
    count +=1
    line = original.readline()
    if not line:
        break
    addLine.writelines(str(count) + '\t' + line.rstrip() +'\n')
original.close()
addLine.close()