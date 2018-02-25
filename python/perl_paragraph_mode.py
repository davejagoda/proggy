#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', help='file to process')
parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
args = parser.parse_args()
if args.verbose: print('about to begin')
with open(args.file, 'r') as f:
    all_data = f.read()
paragraphs = all_data.split('\n\n')
print((len(paragraphs)))
if args.verbose: print('about to end')
