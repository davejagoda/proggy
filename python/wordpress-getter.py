#!/usr/bin/env python3

import hashlib

import bs4
import requests

URL = "https://wordpress.org/download/release-archive/"


def parse_table(soup):
    table = soup.find("table")
    for tr in table.find_all("tr"):
        td = tr.find_all("td")
        if 4 == len(td):
            lst = td[0].text.split(".")
            if 1 < int(lst[0]):
                print(td[0].text)
                a = td[1].find_all("a")
                assert 3 == len(a)
                url = a[0]["href"]
                filename = url.split("/")[-1]
                print(filename)
                r = requests.get(url, stream=True)  # link to the zip
                assert 200 == r.status_code
                data = r.raw.read()
                m = hashlib.sha1(data)
                derived_hash = m.hexdigest()
                r = requests.get(a[2]["href"])  # link to the shasum
                assert 200 == r.status_code
                downloaded_hash = r.text
                assert derived_hash == downloaded_hash
                with open(filename, "wb") as f:
                    f.write(data)


if "__main__" == __name__:
    r = requests.get(URL)
    assert 200 == r.status_code
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    parse_table(soup)
