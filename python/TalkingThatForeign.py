#!/usr/bin/env python3

import re
import subprocess
import sys

stdout = subprocess.check_output(["say", "-v", "?"], universal_newlines=True)

if 2 == len(sys.argv):
    pattern = sys.argv[1]
else:
    pattern = "en_US"

for line in stdout.splitlines():
    if len(line) > 0:
        (left, right) = line.split("#")
        if None == re.search(pattern, left):
            leftsplit = left.split(" ")
            print(leftsplit[0], right)
            subprocess.call(["say", "-v", leftsplit[0], right])
