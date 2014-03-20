#!/usr/bin/python

import unicodedata

def get_unicode_using_unicode_escape(n):
    s = "%x" % n
    return ('\U' + s.zfill(8)).decode('unicode-escape')

def print_unicode_entry(n):
    u = get_unicode_using_unicode_escape(n)
    print '{:8d} {:8x}'.format(n, n),
    print u.encode('utf8'), unicodedata.category(u),
    try:
        print unicodedata.name(u),
    except:
        print 'unicodedata has no name defined',
    try:
        print unicodedata.digit(u)
    except:
        print 'unicodedata has no numeric value'

if __name__ == '__main__':
    print_unicode_entry(0x4e00)
