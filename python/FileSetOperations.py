#!/usr/bin/python

import argparse, re

def handleArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('f1', help='first file to check')
    parser.add_argument('f2', help='second file to check')
    parser.add_argument('-d', '--difference', action='store_true', help='show the difference of the 2 files')
    parser.add_argument('-i', '--intersection', action='store_true', help='show the intersection of the 2 files')
    parser.add_argument('-u', '--union', action='store_true', help='show the union of the 2 files')
    parser.add_argument('-v', '--verbose', action='store_true', help='show the sets generated from the files')
    args = parser.parse_args()
    return(args.f1, args.f2, args.difference, args.intersection, args.union, args.verbose)

def fileToSet(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
    return(set(lines))

def printed_nicely(label, s):
    print('{}:'.format(label))
    """ Sort the given iterable in the way that humans expect."""
# http://stackoverflow.com/questions/2669059/how-to-sort-alpha-numeric-set-in-python
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    for item in sorted(s, key = alphanum_key):
        print(' {}'.format(item))

if '__main__' == __name__:
    (f1, f2, diff, inter, union, verbose) = handleArguments()
    s1 = fileToSet(f1)
    s2 = fileToSet(f2)
    if verbose:
        printed_nicely('s1', s1)
        printed_nicely('s2', s2)
    if diff:
        printed_nicely('s1-s2', s1-s2)
        printed_nicely('s2-s1', s2-s1)
    if inter:
        printed_nicely('intersection:', s1&s2)
    if union:
        printed_nicely('union:', s1|s2)
    if s1.issubset(s2) and s2.issubset(s1):
        print('the sets are the same')
    else:
        if s1.issubset(s2):
            print('the first is a subset of the second')
        if s2.issubset(s1):
            print('the second is a subset of the first')
