#!/usr/bin/env python3

import argparse
import codecs

if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file to process")
    parser.add_argument(
        "-c", "--count", action="store_true", help="count the number of chars"
    )
    parser.add_argument("-n", "--nth", help="print the nth char")
    args = parser.parse_args()
    with codecs.open(args.file, "r", encoding="utf-8") as f:
        chars = f.read()
    if args.count:
        print(len(chars))
    if args.nth:
        print(chars[int(args.nth)])
