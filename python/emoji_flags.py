#!/usr/bin/env python3

for i in range(0x1f1e6, 0x1f200):
    for j in range(0x1f1e6, 0x1f200):
        print('{}{}'.format(chr(i), chr(j)))
