#!/usr/bin/python

# http://en.wikipedia.org/wiki/List_of_Unicode_characters

import sys, unicodedata, argparse

def number2u(n):
    if n <= 0xffff:
        print('n <= 0xffff')
        return('U+' + '{0:04x}'.format(n))
    else:
        print('n > 0xffff')
        return('U+' + '{0:05x}'.format(n))

def unicode2desc(u):
    return(unicodedata.name(u))

def process_argument(arg):
    print('argument: ' + arg + ' argument length ' + str(len(arg)))
    unicode_string = arg.decode('utf-8')
    for u in unicode_string:
        print(number2u(ord(u)) + ' ' + u + ' &#' + str(ord(u)) + ';')
        print(unicode2desc(u))

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('arg', nargs='*')
    args = parser.parse_args()
    for arg in args.arg:
        process_argument(arg)
