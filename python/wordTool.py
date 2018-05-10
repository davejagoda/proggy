#!/usr/bin/env python3

import argparse

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to process')
    parser.add_argument('-c', '--count', action='store_true',
                        help='count the number of words')
    parser.add_argument('-l', '--length', type=int,
                        help='print words with the given length')
    parser.add_argument('-m', '--measure', action='store_true',
                        help='show length of the shortest and longest words')
    parser.add_argument('-n', '--nth', type=int, help='print the nth word')
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        words = f.read().split()
    if args.count:
        print(len(words))
    if args.measure:
        min = len(words[0])
        max = len(words[0])
        for word in words[1:]:
            if len(word) > max: max = len(word)
            if len(word) < min: min = len(word)
        print('longest word:{} shortest word:{}'.format(max, min))
    if args.nth:
        print(words[args.nth])
    if args.length:
        for word in words:
            if len(word) == args.length:
                print(word)
