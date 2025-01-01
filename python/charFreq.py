#!/usr/bin/env python3

import argparse
import codecs

if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file to process")
    args = parser.parse_args()
    with codecs.open(args.file, "r", encoding="utf-8") as f:
        chars = f.read()
    d = {}
    for c in chars:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for k in sorted(d.keys()):
        if ord(k) < 32:
            c = "\\" + chr(96 + ord(k))
        else:
            c = k
        print("{}:{}".format(c, d[k]))
