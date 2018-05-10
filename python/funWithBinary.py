#!/usr/bin/env python3

def bitCheck(i):
    print('{:2d} {:x} {:4b}'.format(i, i, i), end=' ')
    j = 1
    while True:
        if i & j:
            print('tail', end=' ')
        else:
            print('head', end=' ')
        j *= 2
        if j > i:
            break
    print()

print('dd x bbbb')
for i in range(16):
    bitCheck(i)
