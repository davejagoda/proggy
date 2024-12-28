#!/usr/bin/env python3

for i in range(0x1F1E6, 0x1F200):
    for j in range(0x1F1E6, 0x1F200):
        print("{}{}".format(chr(i), chr(j)))
