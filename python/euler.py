#!/usr/bin/python

import sys, math

def fac(n):
    if (type(n) is not int) or (n < 0):
        sys.exit(1)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    e = 0
    i = 0
    done = False
    while (not done):
        try:
            print(("%1.60f" % (1.0 / fac(i))))
            e += 1.0 / fac(i)
            print(("%1.60f" % e))
            i += 1
        except:
            done = True

    print(("%1.60f <- math.e" % math.e))
