#!/usr/bin/env python3

import sys

while len(sys.argv):
    print(len(sys.argv) - 1, sys.argv.pop())
