#!/usr/bin/python

import argparse

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to process')
    parser.add_argument('-c', '--count', action='store_true', help='count the number of words')
    parser.add_argument('-n', '--nth', help='print the nth word')
    parser.add_argument('-l', '--length', type=int, help='print words with the given length')
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        words = f.read().split()
    if args.count:
        print(len(words))
    if args.nth:
        print(words[int(args.nth)])
    if args.length:
        for word in words:
            if len(word) == args.length:
                print(word)
