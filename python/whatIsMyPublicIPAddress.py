#!/usr/bin/env python3

import urllib.request
import re

f = urllib.request.urlopen('http://davejagoda.nfshost.com/dynamic.php')
pat = r'^\d+\.\d+\.\d+\.\d+'
ip = None

for line in f.read().decode('utf-8').split('\n'):
    if 'REMOTE_ADDR' in line:
        parts = line.split(':')
        assert(2 == len(parts))
        if None == ip:
            ip = re.match(pat, parts[1]).group(0)
        else:
            assert(re.match(pat, parts[1]).group(0) == ip)
print(ip)
