#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, requests, bs4

BASEURL = 'https://en.wikipedia.org'

def parse_table(soup, verbose=False):
    results = []
    # get the last table
    table = soup.find_all('table', 'wikitable sortable')[-1]
    if verbose: print(table)
    row_num = 0
    for tr in table.find_all('tr'):
        if verbose: print(tr)
        td = tr.find_all('td')
        if 0 == len(td) and 0 == row_num:
            if verbose: print('header!')
        else:
            results.append((td[1].text, td[0].text))
        row_num += 1
    return(results)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
    args = parser.parse_args()
    URL = BASEURL + '/wiki/ISO_3166-1'
    r = requests.get(URL)
    if args.verbose: print(r.status_code)
    assert(200 == r.status_code)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    if args.verbose: print(soup)
    broken_bar = unichr(0x00a6)
    for row in parse_table(soup, args.verbose):
        print(broken_bar.join(row))
