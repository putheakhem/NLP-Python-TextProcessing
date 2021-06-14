#!/usr/bin/env python

"""Merge File into Single File"""

__author__      = "Khem Puthea"
__copyright__   = "Copyright 2021, puthea.khem@gmail.com"

import sys

input_file = open(sys.argv[-2], 'r', encoding='utf-8')
output_file = open(sys.argv[-1], 'w', encoding='utf-8')

count = 0
while True:
    count +=1
    line = input_file.readline()
    if not line:
        break
    output_file.writelines('<s> ' + line.rstrip() +' </s>\n')
input_file.close()
output_file.close()