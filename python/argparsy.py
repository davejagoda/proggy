#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("source", nargs="+", help="the source[s]")
parser.add_argument("destination", nargs=1, help="the destination directory")
# mv [-f | -i | -n] [-v] source ... directory
parser.add_argument("-v", "--verbosity", action="count", default=0, help="verbosity")
args = parser.parse_args()
if args.verbosity > 0:
    print("about to echo arguments")
print("source[s]:{}".format(args.source))
print("destination:{}".format(args.destination))
if args.verbosity > 0:
    print("just echoed arguments")
