#!/usr/bin/env python3

import argparse

import bs4
import requests

URL = "https://www.nationalnanpa.com/enas/geoAreaCodeNumberReport.do"


def parse_table(soup, verbose=False):
    results = []
    table = soup.find("table", align="center")
    if verbose:
        print(table.attrs)
    for tr in table.find_all("tr"):
        if verbose:
            print(tr)
        td = tr.find_all("td")
        if 2 > len(td) or "NPA" == td[0].text:
            if verbose:
                print("header!")
        else:
            results.append((td[0].text.strip(), td[1].text.strip()))
    return results


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="show verbose output"
    )
    args = parser.parse_args()
    r = requests.get(URL)
    if args.verbose:
        print(r.status_code)
    assert 200 == r.status_code
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    if args.verbose:
        print(soup)
    broken_bar = chr(0x00A6)
    for row in parse_table(soup, args.verbose):
        print(broken_bar.join(row))
