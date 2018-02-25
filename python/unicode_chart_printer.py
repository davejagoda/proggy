#!/usr/bin/env python3

import argparse
import unicodedata

def make_table_of_ranges():
    ranges = {}
    ranges['arabic']     = (0x0600,0x06ff)
    ranges['bengali']    = (0x0980,0x09ff)
    ranges['devanagari'] = (0x0900,0x097f)
    ranges['greek']      = (0x0370,0x03ff)
    ranges['gurmukhi']   = (0x0a00,0x0a7f)
    ranges['hebrew']     = (0x0590,0x05ff)
    ranges['sinhala']    = (0x0d80,0x0dff)
    ranges['tamil']      = (0x0b80,0x0bff)
    ranges['telugu']     = (0x0c00,0x0c7f)
    return(ranges)

def print_range(lo, hi):
    for i in range(lo, hi+1):
        c = chr(i)
        try:
            name = unicodedata.name(c)
        except:
            name = 'NONE'
        print((i, hex(i), c))
#        print(i, hex(i), c, name)

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
