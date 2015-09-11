#!/usr/bin/python

import sys

def factorial(n):
    retValue = 1
    for i in range(2, n + 1):
        retValue *= i
    return(retValue)

if '__main__' == __name__:
    assert 2 == len(sys.argv)
    print(factorial(int(sys.argv[1])))
