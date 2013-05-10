#!/usr/bin/python

import sys, unicodedata

for arg in sys.argv[1:]:
    print('argument: ' + arg + ' argument length ' + str(len(arg)))
    unicode_string = arg.decode('utf-8')
    for u in unicode_string:
        print(u + ' ' + str(ord(u)) + ' ' + hex(ord(u)))
