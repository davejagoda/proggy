#!/usr/bin/env python3

import sys

if '__main__' == __name__:
    for filename in sys.argv[1:]:
        print(f'processing:{filename}')
        with open(filename, newline='') as f:
            if '\r' in f.read():
                print(f'file:{filename} contains a carriage return')
