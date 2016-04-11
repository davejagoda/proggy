#!/usr/bin/python

import subprocess, sys, re

stdout = subprocess.check_output(['say', '-v', '?'])

if (2 == len(sys.argv)):
    pattern = sys.argv[1]
else:
    pattern = 'en_US'

for line in stdout.split('\n'):
    if len(line) > 0:
        (left,right) = line.split('#')
        if (None == re.search(pattern, left)):
            leftsplit=left.split(' ');
            print leftsplit[0], right
            subprocess.call(['say', '-v', leftsplit[0], right])