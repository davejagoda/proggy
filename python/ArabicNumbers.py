#!/usr/bin/env python3

import unicodedata


def print_unicode_entry(n):
    u = chr(n)
    try:
        print(unicodedata.digit(u), end=" ")
    except:
        return False
    print("{:4d} 0x{:3x}".format(n, n), u, unicodedata.category(u), unicodedata.name(u))
    return True


if __name__ == "__main__":
    i = 0x660
    done = False
    while not done:
        if print_unicode_entry(i):
            i += 1
        else:
            done = True
