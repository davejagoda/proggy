#!/usr/bin/python

import unicodedata

for i in xrange(0xc00,0xc80):
    print i, hex(i), unichr(i).encode('utf8')
#    try:
#        print i, hex(i), unichr(i).encode('utf8'), unicodedata.name(unichr(i))
#    except:
#        print "NO NAME"
