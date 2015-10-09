#!/usr/bin/python

for _ in range(0x1f4b4,0x1f4b8):
    print(unichr(_).encode('utf8'))
