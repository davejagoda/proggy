#!/usr/bin/env python3

import datetime, sys

if 1 == len(sys.argv):
    epoch = datetime.datetime.utcnow()
else:
    try:
        epoch = datetime.datetime.fromtimestamp(float(sys.argv[1]))
    except:
        epoch = datetime.datetime.fromtimestamp(float(sys.argv[1])/1000.0)

print(epoch.replace(microsecond=0).isoformat()+'Z')
