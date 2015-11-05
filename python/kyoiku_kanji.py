#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, bs4

URL = 'https://en.wikipedia.org/wiki/Ky%C5%8Diku_kanji'

if '__main__' == __name__:
    r = requests.get(URL)
    assert(200 == r.status_code)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    t = soup.find('span', id='First_grade_.2880_kanji.29')
    found_it = False
    while not found_it:
        if u'table' == t.name:
            found_it = True
        else:
            t = t.next_element
    for tr in t.find_all('tr'):
        td = tr.find_all('td')
        cell_pos = 0
        output = []
        for cell in td:
            if 1 == cell_pos or 3 == cell_pos:
                output.append(cell.text)
            cell_pos += 1
        if output:
            print(':'.join(output))
