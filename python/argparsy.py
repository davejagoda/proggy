#!/usr/bin/python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("-v", "--verbose", action="store_true", help="show verbose output")
args = parser.parse_args()
if args.verbose:
    print "about to echo argments"
print args.echo
if args.verbose:
    print "just echoed argments"
