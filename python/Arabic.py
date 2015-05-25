#!/usr/bin/python

import unicodedata

for i in xrange(0x600,0x700):
    print i, hex(i), unichr(i).encode('utf8')
#    try:
#        print i, hex(i), unichr(i).encode('utf8'), unicodedata.name(unichr(i))
#    except:
#        print "NO NAME"
