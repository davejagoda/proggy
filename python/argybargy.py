#!/usr/bin/python

import sys

while len(sys.argv):
    print len(sys.argv) - 1, sys.argv.pop()
