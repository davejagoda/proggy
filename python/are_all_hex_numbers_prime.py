#!/usr/bin/env python3

import math

def is_prime(n):
    i = 2
    while i < math.sqrt(n):
        print('checking if {} is prime by dividing by {}'.format(n, i))
        if 0 == n % i:
            print('not prime: {} is divided evenly by {}'.format(n, i))
            return(False)
        i += 1
    return(True)

x = 1
i = 1
while is_prime(x):
    print('{}:{:3d}'.format(i, x))
    x += 6 * i
    i += 1
