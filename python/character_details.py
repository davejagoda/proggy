#!/usr/bin/env python3

# http://en.wikipedia.org/wiki/List_of_Unicode_characters

import sys, unicodedata, argparse


def number2u(n):
    if n <= 0xFFFF:
        print("n <= 0xffff")
        return "U+{0:04x}".format(n)
    else:
        print("n > 0xffff")
        return "U+{0:05x}".format(n)


def unicode2desc(u):
    return unicodedata.name(u)


def process_unicode_string(unicode_string):
    for u in unicode_string:
        print("{} {} &#{};".format(number2u(ord(u)), u, str(ord(u))))
        print(unicode2desc(u))


def process_argument(arg):
    print("processing argument: {} argument length: {}".format(arg, len(arg)))
    process_unicode_string(arg)


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("arg", nargs="*")
    args = parser.parse_args()
    for arg in args.arg:
        process_argument(arg)
