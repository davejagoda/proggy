#!/usr/bin/python

import sys, string, codecs, unicodedata

for file in sys.argv[1:]:
    linecount = 0
    with codecs.open(file, 'r', 'utf8') as f:
        for line in f.readlines():
            linecount += 1
            for datum in line:
                if datum not in string.printable:
                    try:
                        print('line:{} -> {}:{}'.format(linecount, datum.encode('utf8'), unicodedata.name(datum)))
                    except:
                        print('line:{} -> {}:{}'.format(linecount, datum.encode('utf8'), 'no such unicode name exists'))
