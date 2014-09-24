#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this prints out checked out books from SCCL

from bs4 import BeautifulSoup
import sys, getpass, urllib, urllib2, re

if len(sys.argv) < 2:
    print('Usage: ' + sys.argv[0] + ' username [username ...]')
    sys.exit(1)

login = 'https://sccl.bibliocommons.com/user/login'
checkedout = 'http://sccl.bibliocommons.com/checkedout'
fines = 'https://sccl.bibliocommons.com/fines'
logout = 'https://sccl.bibliocommons.com/user/logout'
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
password = getpass.getpass()
for username in sys.argv[1:]:
    print('USER: ' + username)
    values = { 'name' : username,
               'user_pin' : password }
    data = urllib.urlencode(values)
    r = opener.open(login, data)
    r = opener.open(checkedout)
    soup = BeautifulSoup(r.read())
#    print(soup.prettify().encode('utf8'))
    logged_in_user = soup.find(text=re.compile('Logged in as '))
    print('User: ' + logged_in_user)
#   <a class="jacketCoverLink" href="/item/show/973973016_office_space" target="_parent" title="Office Space">
    for c in soup.find_all('a', 'jacketCoverLink'):
        d = c.parent
#       <span class="value overdue">
#       <span class="value coming_due">
        out = d.find_next('span', 'value overdue')
        if out == None:
            out = d.find_next('span', 'value coming_due')
#        print('UNIT:' + out.get_text().encode('utf8') + c['title'])
        print('UNIT: ' + out.get_text() + ' ' +  c['title'])
    r = opener.open(fines)
    soup = BeautifulSoup(r.read())
    fine = soup.find(text=re.compile('\$'))
    print('Fine: ' + fine)
    r = opener.open(logout)
