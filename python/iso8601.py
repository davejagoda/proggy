#!/usr/bin/python

import datetime, sys

if 1 == len(sys.argv):
    epoch = datetime.datetime.utcnow()
else:
    epoch = datetime.datetime.fromtimestamp(float(sys.argv[1]))

print(epoch.replace(microsecond=0).isoformat()+'Z')
