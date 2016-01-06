#!/usr/bin/python

import argparse

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delimiter', help='word delimiter')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('file', help='file to process')
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        lines = f.readlines()
    max_words = len(lines[0].split(args.delimiter))
    min_words = len(lines[0].split(args.delimiter))
    for line in lines:
        max_words = max(max_words, len(line.split(args.delimiter)))
        min_words = min(min_words, len(line.split(args.delimiter)))
    print('max words per line={}'.format(max_words))
    print('min words per line={}'.format(min_words))
