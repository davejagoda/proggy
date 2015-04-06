#!/usr/bin/python

import unicodedata

for i in xrange(0x30a0,0x3100):
    c = unichr(i)
    try:
        name = unicodedata.name(c)
    except:
        name = 'NONE'
    if '' == unicodedata.decomposition(c) and 'LETTER' in name and 'SMALL' not in name:
        print c.encode('utf8')
#        print c.encode('utf8'), name
