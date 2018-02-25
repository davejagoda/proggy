#!/usr/bin/env python

import argparse
import hashlib
import base64

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', type=int, help='how many characters to output')
    parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
    args = parser.parse_args()
    input = eval(input('enter random characters (will be echoed): '))
    h = hashlib.new('sha512')
    h.update(input)
    assert(64 == len(h.digest()))
    output = base64.b64encode(h.digest())
    if args.count:
        print((output[:args.count]))
    else:
        print(output)
