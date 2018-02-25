#!/usr/bin/python
# -*- coding: utf-8 -*-

# this reads a download HTML file of the USNews and World Report top schools
# and prints out the relevant text

from bs4 import BeautifulSoup
import sys

if len(sys.argv) != 2:
    print(("Usage: " + sys.argv[0] + " <filename>"))
    sys.exit(1)

f = open(sys.argv[1])
html_doc = f.read()
soup = BeautifulSoup(html_doc)
# if you just do this:
#   print(soup.prettify())
# you will get this:
#   UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position xxxxx: ordinal not in range(128)
# u'\xe9 is this character: é
#print("here's the whole thing")
#print(soup.prettify().encode('utf8'))
#print("here's the title")
#print(soup.title)

#for span in soup.find_all("span", "rank"):
#    print(span)
for td in soup.find_all("td", "university-name"):
    print((td.a.contents[0].encode('utf8'), ':', td.p.contents[0]))

f.close()
