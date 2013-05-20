#!/usr/bin/python

import unicodedata

for i in xrange(0xff65,0xffa0):
    print i, hex(i), unichr(i).encode('utf8'), unicodedata.name(unichr(i))

# ./HalfWidthKana.py | grep LETTER | grep -v SMALL | wc -l
# returns 46 as expected
