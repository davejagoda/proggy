#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, requests, bs4

URL = 'https://en.wikipedia.org/wiki/Kangxi_radical'

def parse_table(soup):
    results = []
    table = soup.find('table', 'wikitable sortable collapsible')
    for tr in table.find_all('tr'):
        td_count = 0
        row = []
        for td in tr.find_all('td'):
# a better design would be get the column numbers based on the headings
            if 1 == td_count or 7 == td_count:
                row.append(td.text)
            td_count += 1
        if 0 != len(row):
            results.append(row)
    return(results)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
    args = parser.parse_args()
    r = requests.get(URL)
    assert(200 == r.status_code)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    if args.verbose:
        print(soup)
    broken_bar = chr(0x00a6)
    for row in parse_table(soup):
        print((broken_bar.join(row)))
