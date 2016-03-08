#!/usr/bin/python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('source', nargs='+', help='the source[s]')
parser.add_argument('destination', nargs=1, help='the destination directory')
# mv [-f | -i | -n] [-v] source ... directory
parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
args = parser.parse_args()
if args.verbose:
    print('about to echo arguments')
print('source[s]:{}'.format(args.source))
print('destination:{}'.format(args.destination))
if args.verbose:
    print('just echoed arguments')
