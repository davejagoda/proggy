#!/usr/bin/python

import unicodedata

print('- DASH')
print('-- DASH DASH')
for i in range(0x2010,0x2016):
    print((chr(i).encode('utf8') + ' ' + unicodedata.name(chr(i)) + ' U+' + hex(i)))
