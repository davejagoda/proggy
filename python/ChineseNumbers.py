#!/usr/bin/env python3

import unicodedata

def unicode_generator_from_list():
    list_of_chinese_numeral_code_points = [
        0x96F6,
        0x4E00,
        0x4E8C,
        0x4E09,
        0x56DB,
        0x4E94,
        0x516D,
        0x4E03,
        0x516B,
        0x4E5D
        ]
    for n in list_of_chinese_numeral_code_points:
        yield(n)

def print_unicode_entries():
    i = 0
    for n in unicode_generator_from_list():
        u = chr(n)
        print('{} {:4d} 0x{:3x}'.format(i, n, n), u, unicodedata.category(u), unicodedata.name(u))
        i += 1

if __name__ == '__main__':
    print_unicode_entries()
