#!/usr/bin/python

import sys, string, codecs, unicodedata

for file in sys.argv[1:]:
    f = codecs.open(file, 'r', 'utf8')
    for datum in f.read():
        if datum not in string.printable:
            print(datum.encode('utf8') + ':' + unicodedata.name(datum))
    f.close()
