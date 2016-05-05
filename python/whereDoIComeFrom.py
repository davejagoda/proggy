#!/usr/bin/python

# trying to do something like this in a less brittle way:
#last | grep dj | cut -b 23-38 | sort | uniq -c

import subprocess, getpass, pprint

places = {}
stdout = subprocess.check_output(['last'])
lines = stdout.split('\n')
for line in lines:
    words = line.split()
    if words and getpass.getuser() == words[0]:
        if words[2] in places:
            places[words[2]] += 1
        else:
            places[words[2]] = 1
pprint.pprint(places)
