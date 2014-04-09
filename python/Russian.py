#!/usr/bin/python

import unicodedata

for i in xrange(0x0410,0x0450):
    print i, hex(i), unichr(i).encode('utf8'), unicodedata.name(unichr(i))

# ./Russian.py | wc -l
# returns 64 as expected
