#!/usr/bin/env python3

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR

import time

if time.localtime().tm_isdst:
    offset = time.altzone
else:
    offset = time.timezone

if offset > 0:
    sign = "-"
else:
    sign = "+"

# more obvious 'floor' division
hh = abs(int(offset / SECONDS_PER_HOUR))
mm = (abs(offset) - (hh * SECONDS_PER_HOUR)) // SECONDS_PER_MINUTE

print("{}{:02d}:{:02d}".format(sign, hh, mm))

"""
To test:
cd /usr/share/zoneinfo
for i in `find . -print | cut -b 3-`; do echo -n "$i "; TZ=$i /bin/date "+%z"; done > /tmp/sh
for i in `find . -print | cut -b 3-`; do echo -n "$i "; TZ=$i ~/src/github/proggy/python/getTimeZoneOffSet.py | tr -d : ; done > /tmp/py
diff /tmp/sh /tmp/py
"""
