#!/usr/bin/env python3

import datetime, sys

if 1 == len(sys.argv):
    epoch = datetime.datetime.now(datetime.timezone.utc)
else:
    try:
        epoch = datetime.datetime.fromtimestamp(
            float(sys.argv[1]), datetime.timezone.utc
        )
    except:
        epoch = datetime.datetime.fromtimestamp(
            float(sys.argv[1]) / 1000.0, datetime.timezone.utc
        )

print(epoch.replace(microsecond=0).isoformat())
