#!/usr/bin/python

import argparse

def handleArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('f1', help='first file to check')
    parser.add_argument('f2', help='second file to check')
    parser.add_argument('-i', '--intersection', action='store_true', help='show the intersection of the 2 files')
    parser.add_argument('-u', '--union', action='store_true', help='show the union of the 2 files')
    parser.add_argument('-v', '--verbose', action='store_true', help='show the sets generated from the files')
    args = parser.parse_args()
    return(args.f1, args.f2, args.intersection, args.union, args.verbose)

def fileToSet(file):
    f = open(file)
    lines = [line.strip() for line in f.readlines()]
    f.close()
    return(set(lines))

if '__main__' == __name__:
    (f1, f2, inter, union, verbose) = handleArguments()
    s1 = fileToSet(f1)
    s2 = fileToSet(f2)
    if verbose:
        print('s1:'+str(s1))
        print('s2:'+str(s2))
    if inter:
        print('intersection:' + str(s1&s2))
    if union:
        print('union:' + str(s1|s2))
    if s1.issubset(s2) and s2.issubset(s1):
        print('the sets are the same')
    else:
        if s1.issubset(s2):
            print('the first is a subset of the second')
        if s2.issubset(s1):
            print('the second is a subset of the first')
