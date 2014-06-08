#!/usr/bin/python

import argparse

def handleArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('f1', help='first file to check')
    parser.add_argument('f2', help='second file to check')
    args = parser.parse_args()
    return(args.f1, args.f2)

def fileToSet(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    return(set(lines))

if '__main__' == __name__:
    (f1, f2) = handleArguments()
    s1 = fileToSet(f1)
    s2 = fileToSet(f2)
#    print('s1:'+str(s1))
#    print('s2:'+str(s2))
#    print('intersection:'+str(s1&s2))
#    print('union:'+str(s1|s2))
    if s1.issubset(s2) and s2.issubset(s1):
        print('the sets are the same')
    else:
        if s1.issubset(s2):
            print('the first is a subset of the second')
        if s2.issubset(s1):
            print('the second is a subset of the first')
