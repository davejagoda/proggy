#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, requests, bs4

URL = 'https://en.wikipedia.org/wiki/Ky%C5%8Diku_kanji'

def parse_one_section(section):
    results = []
    found_it = False
    while not found_it:
        if u'table' == section.name:
            found_it = True
        else:
            section = section.next_element
    for tr in section.find_all('tr'):
        td = tr.find_all('td')
        cell_pos = 0
        output = []
        for cell in td:
            if 1 == cell_pos or 3 == cell_pos:
                output.append(cell.text)
            cell_pos += 1
        if output:
            results.append((output))
    return(results)

def grade_to_anchor(grade):
    g2u = {
        '1': 'First_grade_.2880_kanji.29',
        '2': 'Second_grade_.28160_kanji.29',
        '3': 'Third_grade_.28200_kanji.29',
        '4': 'Fourth_grade_.28200_kanji.29',
        '5': 'Fifth_grade_.28185_kanji.29',
        '6': 'Sixth_grade_.28181_kanji.29'
    }
    return(g2u[grade])

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
    parser.add_argument('grade', help='grade level of kanji (1-6)')
    args = parser.parse_args()
    r = requests.get(URL)
    assert(200 == r.status_code)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    section = soup.find('span', id=grade_to_anchor(args.grade))
    results = parse_one_section(section)
    for row in results:
        print(u':'.join(row))
