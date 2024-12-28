#!/usr/bin/env python3

import argparse
import hashlib
import base64

if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", type=int, help="how many characters to output")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="show verbose output"
    )
    args = parser.parse_args()
    input = input("enter random characters (will be echoed): ")
    h = hashlib.new("sha512")
    h.update(input.encode("utf-8"))
    assert 64 == len(h.digest())
    output = base64.b64encode(h.digest()).decode("utf-8")
    if args.count:
        print(output[: args.count])
    else:
        print(output)
