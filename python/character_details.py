#!/usr/bin/python

# http://en.wikipedia.org/wiki/List_of_Unicode_characters

import sys, unicodedata

def number2u(n):
    if n <= 0xffff:
        print('n <= 0xffff')
        return('U+' + '{0:04x}'.format(n))
    else:
        print('n > 0xffff')
        return('U+' + '{0:05x}'.format(n))

def number2desc(n):
    return(unicodedata.name(u))

for arg in sys.argv[1:]:
    print('argument: ' + arg + ' argument length ' + str(len(arg)))
    unicode_string = arg.decode('utf-8')
    for u in unicode_string:
        print(number2u(ord(u)) + ' ' + u + ' &#' + str(ord(u)) + ';')
        print(number2desc(ord(u)))
