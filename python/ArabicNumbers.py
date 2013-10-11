#!/usr/bin/python

import unicodedata

def get_unicode_using_unicode_escape(n):
    s = "%x" % n
    return ('\U' + s.zfill(8)).decode('unicode-escape')

def print_unicode_entry(n):
    u = get_unicode_using_unicode_escape(n)
    try:
        print unicodedata.digit(u),
    except:
        return False
    print '{:4d} 0x{:3x}'.format(n, n), u.encode('utf8'), unicodedata.category(u), unicodedata.name(u)
    return True

if __name__ == '__main__':
    i = 0x660
    done = False
    while (not done):
        if (print_unicode_entry(i)):
            i += 1
        else:
            done = True
