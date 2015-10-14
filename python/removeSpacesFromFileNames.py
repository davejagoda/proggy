#!/usr/bin/python

import sys, os

for filename in sys.argv[1:]:
    if ' ' in filename:
        newname = filename.replace(' ', '')
        os.rename(filename, newname)
