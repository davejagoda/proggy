#!/usr/bin/env python3

import sys

if 2 != len(sys.argv):
    print("need exactly one argument - a file to destroy")
    sys.exit(1)

filename = sys.argv[1]
with open(filename, "r+b") as f:
    octets = f.read()
    f.seek(0)
    for octet in octets:
        print((chr(octet), octet, (octet + 1) % 255))
        f.write(bytes([(octet + 1) % 255]))
