#!/usr/bin/env python3

import argparse
import unicodedata

def make_table_of_characters():
    characters = {}
    characters['all']                   = 0x00000
    characters['businessmanlevitating'] = 0x1f574
    characters['copyright']             = 0x000a9
    characters['floppy']                = 0x1f4be
    characters['heart']                 = 0x02665
    characters['middlefinger']          = 0x1f595
    characters['infinity']              = 0x0221e
    characters['interrobang']           = 0x0203d
    characters['nj']                    = 0x001cc
    characters['pi']                    = 0x003a0
    characters['poo']                   = 0x1f4a9
    characters['radical']               = 0x0221a
    characters['tengu']                 = 0x1f47a
    return(characters)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    characters = make_table_of_characters()
    for r in characters.keys():
        arg_name = '--{}'.format(r)
        parser.add_argument(arg_name, action='store_true')
    args = parser.parse_args()
    for k, v in args.__dict__.items():
        if args.all or v:
            print(chr(characters[k]), ' ', end='')
    print()
