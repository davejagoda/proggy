#!/usr/bin/env python3

import sys, re

if 2 != len(sys.argv):
    print('need exactly one argument - a VCS calendar file to fix')
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r') as f:
    lines = f.readlines()

with open(filename, 'w') as f:
    for line in lines:
        match = re.search('^End:(.*)$', line)
        if match:
            f.write('END:' + match.group(1) + '\n')
        else:
            f.write(line)
