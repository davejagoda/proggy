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
    g2u = [
        'All',
        'First_grade_.2880_kanji.29',
        'Second_grade_.28160_kanji.29',
        'Third_grade_.28200_kanji.29',
        'Fourth_grade_.28200_kanji.29',
        'Fifth_grade_.28185_kanji.29',
        'Sixth_grade_.28181_kanji.29'
    ]
    return(g2u[grade])

def get_one_section(soup, grade):
    return(parse_one_section(soup.find('span', id=grade_to_anchor(grade))))

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
    parser.add_argument('grade', type=int, choices=[x for x in range(7)], help='grade level of kanji (1-6, 0 for all)')
    args = parser.parse_args()
    r = requests.get(URL)
    assert(200 == r.status_code)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    if args.grade:
        for row in get_one_section(soup, args.grade):
            print(u':'.join(row))
    else:
        for grade in range(1,7):
            for row in get_one_section(soup, grade):
                print(u"['{}','{}',{}]".format(row[0],row[1],grade))
