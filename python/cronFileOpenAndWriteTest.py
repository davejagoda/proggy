#!/usr/bin/env python3

import datetime

t = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

modes = ["a", "w"]
directories = ["/tmp", "/home/dj", "/home/dj/log"]

for m in modes:
    for d in directories:
        n = d + "/" + t
        f = open(n, m)
        f.write(t)
        f.write("\n")
        f.close()
