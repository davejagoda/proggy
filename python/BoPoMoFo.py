#!/usr/bin/python

import unicodedata

def display(i):
    print i, hex(i), unichr(i).encode('utf8'),
    try:
        print unicodedata.name(unichr(i))
    except:
        print 'UNKNOWN NAME'

print 'original range'
for i in xrange(0x3105,0x312e):
    display(i)

print 'extended range'
for i in xrange(0x31a0,0x31bb):
    display(i)
