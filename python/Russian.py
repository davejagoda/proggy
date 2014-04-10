#!/usr/bin/python

import unicodedata, argparse
parser = argparse.ArgumentParser()
parser.add_argument("--yo", action="store_true", help="show yo")
args = parser.parse_args()

alpha = range(0x0410,0x0450)
if args.yo:
    alpha.insert(38,0x451)
    alpha.insert( 6,0x401)
for i in alpha:
    print i, hex(i), unichr(i).encode('utf8'), unicodedata.name(unichr(i))

# ./Russian.py | wc -l
# returns 64 as expected

# ./Russian.py --yo | wc -l
# returns 66 as expected

