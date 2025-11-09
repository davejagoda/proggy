#!/usr/bin/env python3

import datetime
import sys

for unix_time in sys.argv[1:]:
    # check for time in milliseconds, will break after year 9999
    if 13 == len(unix_time):
        unix_time = unix_time[:10]
    print(
        datetime.datetime.isoformat(
            datetime.datetime.fromtimestamp(float(unix_time), datetime.UTC)
        )
    )
