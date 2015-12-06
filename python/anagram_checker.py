#!/usr/bin/python

import argparse, collections

def arg_to_collection(arg):
    ctr = collections.Counter()
    for c in arg:
        if c.isalpha(): ctr[c.lower()] += 1
    return(ctr)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('s1')
    parser.add_argument('s2')
    args = parser.parse_args()
    if arg_to_collection(args.s1) == arg_to_collection(args.s2):
        print('anagram!')
    else:
        print('not anagram')
