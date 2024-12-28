#!/usr/bin/env python3

import argparse, requests, bs4

BASEURL = "https://en.wikipedia.org"


def parse_subtable(soup, verbose=False):
    results = []
    tables = soup.find_all("table", "wikitable sortable")
    if verbose:
        print(tables)
    if [] == tables:
        return results
    for table in tables:
        row_num = 0
        for tr in table.find_all("tr"):
            if verbose:
                print(tr)
            td = tr.find_all("td")
            if 0 == len(td) and 0 == row_num:
                if verbose:
                    print("header!")
            else:
                key = td[0].text.split(" ")[0]
                value = " ".join(td[1].text.split("\n")).strip()
                results.append((key, value))
            row_num += 1
    return results


def parse_table(soup, verbose=False):
    results = []
    table = soup.find("table", "wikitable sortable")
    if verbose:
        print(table)
    row_num = 0
    for tr in table.find_all("tr"):
        if verbose:
            print(tr)
        td = tr.find_all("td")
        if 0 == len(td) and 0 == row_num:
            if verbose:
                print("header!")
        else:
            results.append(td[0].a["href"])
        row_num += 1
    return results


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="show verbose output"
    )
    args = parser.parse_args()
    URL = BASEURL + "/wiki/ISO_3166-2"
    r = requests.get(URL)
    if args.verbose:
        print(r.status_code)
    assert 200 == r.status_code
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    if args.verbose:
        print(soup)
    broken_bar = chr(0x00A6)
    for row in parse_table(soup, args.verbose):
        URL = BASEURL + row
        r = requests.get(URL)
        if args.verbose:
            print(r.status_code)
        assert 200 == r.status_code
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        if args.verbose:
            print(soup)
        for subrow in parse_subtable(soup, args.verbose):
            print(broken_bar.join(subrow))
