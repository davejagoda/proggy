#!/usr/bin/python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', help='echo the string you use here')
args = parser.parse_args()

with open(args.file, 'r') as f:
    for line in f.readlines():
        print(('    {}'.format(line.rstrip())))
