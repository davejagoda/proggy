#!/usr/bin/env python3

"""
try this

OS X 11.5.2:
grep -r %Y- /usr/share/locale
/usr/share/locale/sv_SE.ISO8859-15/LC_TIME:%Y-%m-%d
/usr/share/locale/sv_SE.ISO8859-1/LC_TIME:%Y-%m-%d

LANG=ja_JP.UTF-8 ./dates_and_locales.py
LANG=sv_SE.ISO8859-1 ./dates_and_locales.py

Ubuntu 21.04:
sudo apt-get install language-pack-hi
sudo apt-get install language-pack-ja
sudo apt-get install language-pack-sv

LANG=hi_IN.utf8 ./dates_and_locales.py
LANG=ja_JP.utf8 ./dates_and_locales.py
LANG=sv_SE.utf8 ./dates_and_locales.py
"""

import datetime
import locale

print(locale.getdefaultlocale())
locale.setlocale(locale.LC_ALL, '')
print(locale.getlocale())
t = datetime.datetime.now()
print(t.isoformat(timespec='seconds'))
print(t.strftime('%x %X'))
print(t.strftime('%EY'))
print(t.strftime('%a'))
print(locale.currency(1, grouping=True))
print(locale.currency(1000, grouping=True))
print(locale.currency(10000, grouping=True))
print(locale.currency(1000000000, grouping=True))
