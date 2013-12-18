#!/usr/bin/python

import subprocess, re

stdout = subprocess.check_output(['say', '-v', '?'])

for line in stdout.split('\n'):
    if len(line) > 0:
        (left,right) = line.split('#')
        if (None == re.search('en_US', left)):
            leftsplit=left.split(' ');
            print leftsplit[0], right
            subprocess.call(['say', '-v', leftsplit[0], right])
