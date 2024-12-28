#!/usr/bin/env python3

"""
Ubuntu 21.04:
sudo apt-get install language-pack-ja

output:
backwards
令和 2021-09-26 令和03年
平成 2019-04-30 平成31年
昭和 1989-01-07 昭和64年
大正 1926-12-24 大正15年
明治 1912-07-29 明治45年
西暦 1872-12-31 西暦1872年
0001-01-01
forwards
西暦 0001-01-01 西暦01年
明治 1873-01-01 明治06年
大正 1912-07-30 大正元年
昭和 1926-12-25 昭和元年
平成 1989-01-08 平成元年
令和 2019-05-01 令和元年
2021-09-28
"""

import datetime
import locale

locale.setlocale(locale.LC_ALL, "ja_JP.UTF-8")
t = datetime.date.today()
tomorrow = t + datetime.timedelta(days=1)

print("backwards")
era = ""
while True:
    if era != t.strftime("%EY")[:2]:
        era = t.strftime("%EY")[:2]
        year = t.strftime("%EY")
        print(f"{era} {t} {year}")
    try:
        t = t - datetime.timedelta(days=1)
    except:
        print(t)
        break

print("forwards")
era = ""
while True:
    if era != t.strftime("%EY")[:2]:
        era = t.strftime("%EY")[:2]
        year = t.strftime("%EY")
        print(f"{era} {t} {year}")
    t = t + datetime.timedelta(days=1)
    if t > tomorrow:
        print(t)
        break
