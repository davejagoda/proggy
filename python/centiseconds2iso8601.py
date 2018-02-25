#!/usr/bin/python

import datetime, sys

for date in sys.argv[1:]:
    print((datetime.datetime.fromtimestamp(float(date)/100)))
