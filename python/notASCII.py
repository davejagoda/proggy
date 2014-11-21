#!/usr/bin/python

import sys, string, codecs

for file in sys.argv[1:]:
    f = codecs.open(file, 'r', 'utf8')
    for datum in f.read():
        if datum not in string.printable:
            print(datum.encode('utf8'))
    f.close()
