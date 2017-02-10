#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import random

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
    args = parser.parse_args()
    with(open(args.file, 'r')) as f:
         nodes = f.read().splitlines()
    if args.verbose: print(len(nodes))
    src = nodes.pop(int(random.randrange(len(nodes))))
    while (len(nodes) > 0):
        dst = nodes.pop(int(random.randrange(len(nodes))))
        print('{}:{}'.format(src,dst))
        src = dst
