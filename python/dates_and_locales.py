#!/usr/bin/env python3

"""
try this
LANG=ja_JP.UTF-8 ./dates_and_locales.py

OS X 11.5.2:
grep -r %Y- /usr/share/locale
/usr/share/locale/sv_SE.ISO8859-15/LC_TIME:%Y-%m-%d
/usr/share/locale/sv_SE.ISO8859-1/LC_TIME:%Y-%m-%d

LANG=sv_SE.ISO8859-1 ./dates_and_locales.py

Ubuntu 21.04:
sudo apt-get install language-pack-ja
sudo apt-get install language-pack-hi

LANG=hi_IN.utf8 ./dates_and_locales.py
"""

import datetime
import locale

print(locale.getdefaultlocale())
locale.setlocale(locale.LC_ALL, '')
print(locale.getlocale())
t = datetime.datetime.now()
print(t.isoformat(timespec='seconds'))
print(t.strftime('%x %X'))
print(locale.currency(1))
print(locale.currency(1000))
print(locale.currency(10000))
print(locale.currency(1000000000))
