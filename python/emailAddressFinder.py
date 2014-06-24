#!/usr/bin/python

import sys, re

f = open(sys.argv[1])
for line in f.readlines():
    p = re.search('(\S*@\S*)', line)
    if (p):
        print(p.group(1))
