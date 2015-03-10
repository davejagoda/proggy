#!/usr/bin/python
# -*- coding: utf-8 -*-

# Linux file systems:
# give back whatever you receive
# when creating, make NFC files

# Apple file systems:
# give back NFD whatever you receive
# when creating, make NFC files

# references:
# http://en.wikipedia.org/wiki/Unicode_equivalence
# http://www.win.tue.nl/~aeb/linux/uc/nfc_vs_nfd.html

import os

def isAscii(s):
    for c in s:
        if (ord(c) > 127):
            return(False)
    return(True)

def Spanish():
# José vs Jose + combining accent
    with open('José', 'a') as f:
        f.write('José')
        f.write('\n')
    jose = 'Jose' + unichr(0x301)
    with open(jose, 'a') as f:
        f.write(jose.encode('utf8'))
        f.write('\n')

def catalog(path):
    print(path)
    for root, dirs, files in os.walk(path):
        print 'root', root, 'dirs', dirs, 'files', files
        for entry in files:
            if (isAscii(entry)):
                pass
            else:
                print('notAlpha', entry)

if '__main__' == __name__:
    Spanish()
    catalog('.')
