#!/usr/bin/python

import unicodedata

print('- DASH')
print('-- DASH DASH')
for i in xrange(0x2010,0x2016):
    print(unichr(i).encode('utf8') + ' ' + unicodedata.name(unichr(i)) + ' U+' + hex(i))
