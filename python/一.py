#!/usr/bin/env python3

import unicodedata

def print_unicode_entry(n):
    u = chr(n)
    print('{:8d} {:8x}'.format(n, n), end=' ')
    print(u, unicodedata.category(u), end=' ')
    try:
        print(unicodedata.name(u), end=' ')
    except:
        print('unicodedata has no name defined', end=' ')
    try:
        print(unicodedata.digit(u))
    except:
        print('unicodedata has no numeric value')

if __name__ == '__main__':
    print_unicode_entry(0x4e00)
