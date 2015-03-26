#!/usr/bin/python

import time

if time.localtime().tm_isdst:
    offset = time.altzone
else:
    offset = time.timezone
hh = offset / -3600
mm = offset % 60
if hh < 0:
    sign = '-'
    hh *= -1
else:
    sign = '+'
print('{}{:02d}:{:02d}'.format(sign,hh,mm))
