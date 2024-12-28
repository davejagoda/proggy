#!/usr/bin/env python3

import os
import sys

lockfile = ".flock"

try:
    f = os.open(lockfile, os.O_CREAT | os.O_EXCL)
except:
    print("failed to lock")
    sys.exit(1)

input("press a key to release lock and exit")

os.close(f)
os.unlink(lockfile)
