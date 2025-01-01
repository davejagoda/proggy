#!/usr/bin/env python3

import re
import urllib.request

f = urllib.request.urlopen("https://davejagoda.nfshost.com/dynamic.php")
pat = r"REMOTE_ADDR:(\S+)<br>"
ip = None

for line in f.read().decode("utf-8").split("\n"):
    if "REMOTE_ADDR" in line:
        if None == ip:
            ip = re.search(pat, line).group(1)
        else:
            assert re.search(pat, line).group(1) == ip
print(ip)
