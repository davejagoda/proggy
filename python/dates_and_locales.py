#!/usr/bin/env python3

"""
try this
LANG=ja_JP.UTF-8 ./dates_and_locales.py
"""

import datetime
import locale

locale.setlocale(locale.LC_ALL, '')
print(locale.getlocale())
t = datetime.datetime.now()
print(t.isoformat(timespec='seconds'))
print(t.strftime('%x %X'))
