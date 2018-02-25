#!/usr/bin/env python3

import argparse
import unicodedata

def make_table_of_ranges():
    ranges = {}
    ranges['hiragana'] = (0x3040, 0x309f)
    ranges['katakana'] = (0x30a0, 0x30ff)
    return(ranges)

def print_range(lo, hi):
    for i in range(lo, hi+1):
        c = chr(i)
        try:
            name = unicodedata.name(c)
        except:
            name = 'NONE'
        if '' == unicodedata.decomposition(c) and 'LETTER' in name and 'SMALL' not in name:
            print(c)
#        print(c.encode('utf8'), name)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    ranges = make_table_of_ranges()
    for r in list(ranges.keys()):
        arg_name = '--{}'.format(r)
        parser.add_argument(arg_name, action='store_true')
    args = parser.parse_args()
    for k, v in list(args.__dict__.items()):
        if v:
            print(k)
            print_range(ranges[k][0], ranges[k][1])
