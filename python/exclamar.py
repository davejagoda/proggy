#!/usr/bin/env python3

import sys

print(" ".join([chr(0x00A1) + arg + chr(0x0021) for arg in sys.argv[1:]]))
