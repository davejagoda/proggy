#!/usr/bin/python

import sys, unicodedata

for arg in sys.argv[1:]:
    print 'argument:',  arg, 'argument length', len(arg)
    unicode_string = arg.decode('utf-8')
    for u in unicode_string:
        print u, ord(u), hex(ord(u))
