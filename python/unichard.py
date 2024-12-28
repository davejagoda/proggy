#!/usr/bin/env python3

import argparse
import unicodedata


def make_table_of_characters():
    characters = {}
    characters["all"] = 0x00000
    characters["bomb"] = 0x1F4A3
    characters["btc"] = 0x020BF
    characters["businessmanlevitating"] = 0x1F574
    characters["cop"] = 0x1F46E
    characters["copyright"] = 0x000A9
    characters["floppy"] = 0x1F4BE
    characters["gun"] = 0x1F52B
    characters["heart"] = 0x02665
    characters["middlefinger"] = 0x1F595
    characters["infinity"] = 0x0221E
    characters["interrobang"] = 0x0203D
    characters["key"] = 0x1F511
    characters["nj"] = 0x001CC
    characters["pi"] = 0x003A0
    characters["poo"] = 0x1F4A9
    characters["radical"] = 0x0221A
    characters["sunglasses"] = 0x1F60E
    characters["tengu"] = 0x1F47A
    return characters


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    characters = make_table_of_characters()
    for r in characters.keys():
        arg_name = "--{}".format(r)
        parser.add_argument(arg_name, action="store_true")
    args = parser.parse_args()
    for k, v in args.__dict__.items():
        if args.all or v:
            print(chr(characters[k]), " ", end="")
    print()
