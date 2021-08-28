#!/usr/bin/env python3

import datetime
import locale

t = datetime.datetime.now()
print(t.isoformat(timespec='seconds'))
print(t.strftime('%x %X'))
print(locale.getlocale())
