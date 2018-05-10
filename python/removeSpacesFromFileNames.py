#!/usr/bin/env python3

import os
import sys

for filename in sys.argv[1:]:
    if ' ' in filename:
        newname = filename.replace(' ', '')
        os.rename(filename, newname)
