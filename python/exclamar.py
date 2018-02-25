#!/usr/bin/python

import sys

print((' '.join([chr(0x00a1).encode('utf8') + arg + chr(0x0021).encode('utf8') for arg in sys.argv[1:]])))
