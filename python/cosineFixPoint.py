#!/usr/bin/env python3

import math

n = 1

while abs(n - math.cos(n)) > 0.000000000000001:
    print(n, n - math.cos(n))
    n = math.cos(n)
