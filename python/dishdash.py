#!/usr/bin/env python3

import unicodedata

print('- DASH')
print('-- DASH DASH')
for i in range(0x2010,0x2016):
    print(chr(i) + ' ' + unicodedata.name(chr(i)) + ' U+' + hex(i))
