#!/usr/bin/env python3

import unicodedata

for i in range(0xff65,0xffa0):
    print(i, hex(i), chr(i), unicodedata.name(chr(i)))

# ./HalfWidthKana.py | grep LETTER | grep -v SMALL | wc -l
# returns 46 as expected
