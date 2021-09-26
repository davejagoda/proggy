#!/usr/bin/env python3

"""
Ubuntu 21.04:
sudo apt-get install language-pack-ja
"""

import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
t = datetime.date.today()
tomorrow = t + datetime.timedelta(days=1)

print('backwards')
era = ''
while True:
    if era != t.strftime('%EY')[:2]:
        era = t.strftime('%EY')[:2]
        year = t.strftime('%EY')
        print(f'{era} {t} {year}')
    try:
        t = t - datetime.timedelta(days=1)
    except:
        print(t)
        break

print('forwards')
era = ''
while True:
    if era != t.strftime('%EY')[:2]:
        era = t.strftime('%EY')[:2]
        year = t.strftime('%EY')
        print(f'{era} {t} {year}')
    t = t + datetime.timedelta(days=1)
    if t > tomorrow:
        print(t)
        break
