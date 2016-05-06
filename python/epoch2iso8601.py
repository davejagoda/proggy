#!/usr/bin/python

import datetime, sys

for date in sys.argv[1:]:
    print(datetime.datetime.isoformat(datetime.datetime.fromtimestamp(float(date))))