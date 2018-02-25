#!/usr/bin/python

import unicodedata

def display(i):
    print(i, hex(i), chr(i).encode('utf8'), end=' ')
    try:
        print(unicodedata.name(chr(i)))
    except:
        print('UNKNOWN NAME')

print('original range')
for i in range(0x3105,0x312e):
    display(i)

print('extended range')
for i in range(0x31a0,0x31bb):
    display(i)
