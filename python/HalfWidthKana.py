#!/usr/bin/python

import unicodedata

for i in range(0xff65,0xffa0):
    print((i, hex(i), chr(i).encode('utf8'), unicodedata.name(chr(i))))

# ./HalfWidthKana.py | grep LETTER | grep -v SMALL | wc -l
# returns 46 as expected
