#!/usr/bin/env python3

"""
OS X 15.2:
grep -r %Y- /usr/share/locale
/usr/share/locale/sv_SE.ISO8859-1/LC_TIME:%Y-%m-%d

LC_ALL=fr_CA.UTF-8 ./dates_and_locales.py
LC_ALL=ja_JP.UTF-8 ./dates_and_locales.py
LC_ALL=sv_SE.ISO8859-1 ./dates_and_locales.py

Ubuntu 22.04:
sudo apt-get install language-pack-fr
sudo apt-get install language-pack-hi
sudo apt-get install language-pack-ja
sudo apt-get install language-pack-sv

LC_ALL=fr_CA.UTF-8 ./dates_and_locales.py
LC_ALL=hi_IN.UTF-8 ./dates_and_locales.py
LC_ALL=ja_JP.UTF-8 ./dates_and_locales.py
LC_ALL=sv_SE.UTF-8 ./dates_and_locales.py
"""

import datetime
import locale

print(locale.getlocale())
locale.setlocale(locale.LC_ALL, "")
print(locale.getlocale())
t = datetime.datetime.fromtimestamp(0, datetime.timezone.utc)
print(t.isoformat(timespec="seconds"))
print(f"%EY: {t.strftime('%EY')}")
print(t.strftime("%a"))
print(t.strftime("%A"))
print(t.strftime("%b"))
print(t.strftime("%B"))
print(t.strftime("%c"))
print(t.strftime("%x %X"))
for n in (1, 3, 4, 9):
    print(f"10 to the {n}: {locale.currency(10**n, grouping=True)}")
