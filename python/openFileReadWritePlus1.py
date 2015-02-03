#!/usr/bin/python

import sys

if 2 != len(sys.argv):
    print('need exactly one argument - a file to destroy')
    sys.exit(1)

with open(sys.argv[1], 'r+b') as f:
    octets = f.read()
    f.seek(0)
    for octet in octets:
        print(octet,ord(octet),ord(octet) + 1 % 255)
        f.write(chr((ord(octet) + 1) % 255))
