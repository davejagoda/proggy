#!/usr/bin/env python3

methods = [
    "st_mode",
    "st_ino",
    "st_dev",
    "st_nlink",
    "st_uid",
    "st_gid",
    "st_size",
    "st_atime",
    "st_mtime",
    "st_ctime",
]

import sys, os

for file in sys.argv[1:]:
    print(file)
    statinfo = os.stat(file)
    print(statinfo)
    for s in methods:
        print(s, ":", getattr(statinfo, s))
