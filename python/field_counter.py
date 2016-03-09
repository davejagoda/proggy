#!/usr/bin/python

import argparse

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delimiter', help='word delimiter')
    parser.add_argument('-l', '--linelength', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('file', help='file to process')
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        lines = f.readlines()
    max_words = len(lines[0].split(args.delimiter))
    min_words = len(lines[0].split(args.delimiter))
    max_line = len(lines[0])
    min_line = len(lines[0])
    for line in lines:
        max_words = max(max_words, len(line.split(args.delimiter)))
        min_words = min(min_words, len(line.split(args.delimiter)))
        max_line = max(max_line, len(line))
        min_line = min(min_line, len(line))
    print('max words per line={}'.format(max_words))
    print('min words per line={}'.format(min_words))
    if args.linelength:
        print('max length line={}'.format(max_line))
        print('min length line={}'.format(min_line))
