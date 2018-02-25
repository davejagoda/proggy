#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import requests
import bs4
import string

BASEURL = 'https://en.wikipedia.org/wiki/List_of_airports_by_IATA_code:_'

def parse_table(soup, verbose=False):
    results = []
    table = soup.find('table', 'wikitable sortable')
    if verbose: print(table)
    row_num = 0
    for tr in table.find_all('tr'):
        if verbose: print(tr)
        td = tr.find_all('td')
        if 0 == len(td):
            if verbose: print('header!')
        else:
            results.append(td[0].text)
        row_num += 1
    return(results)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
    args = parser.parse_args()
    for letter in string.uppercase:
        URL = BASEURL + letter
        if args.verbose: print(URL)
        r = requests.get(URL)
        if args.verbose: print((r.status_code))
        assert(200 == r.status_code)
        soup = bs4.BeautifulSoup(r.content, 'html.parser')
        if args.verbose: print(soup)
        for row in parse_table(soup, args.verbose):
            print((row[:3]))
