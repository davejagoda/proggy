#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this prints out checked out books from SCCL

from bs4 import BeautifulSoup
import sys, os, getpass, urllib, urllib2, re

LOGINURL = 'https://sccl.bibliocommons.com/user/login'
LOGOUTURL = 'https://sccl.bibliocommons.com/user/logout'
CHECKEDOUTURL = 'http://sccl.bibliocommons.com/checkedout?display_quantity=25'
FINESURL = 'https://sccl.bibliocommons.com/fines'
OPENER = urllib2.build_opener(urllib2.HTTPCookieProcessor())

def loginAndReturnSoup(u, p):
    values = { 'name' : u,
               'user_pin' : p }
    data = urllib.urlencode(values)
    r = OPENER.open(LOGINURL, data)
    r = OPENER.open(CHECKEDOUTURL)
    soup = BeautifulSoup(r.read(), 'html.parser')
#    print(soup.prettify().encode('utf8'))
    logged_in_user = soup.find(text=re.compile('Logged in as '))
    try:
        print('User: {}'.format(logged_in_user))
    except:
        print('Bad password')
        sys.exit(1)
    return(soup)

def displayCheckedOut(soup):
#   <a class="jacketCoverLink" href="/item/show/973973016_office_space" target="_parent" title="Office Space">
    for c in soup.find_all('a', 'jacketCoverLink'):
        title = None
        for kid in c.children:
# find the title of the child, if there's more than one child use the last one
            title = kid['title'].encode('utf8')
        d = c.parent
#       <span class="value overdue">
#       <span class="value coming_due">
#       <span class="value out">
        out = d.find_next('span', 'value overdue')
        if out == None:
            out = d.find_next('span', 'value coming_due')
        if out == None:
            out = d.find_next('span', 'value out')
        print('UNIT: {} {}'.format(out.get_text().strip(), title))

def fines():
    r = OPENER.open(FINESURL)
    soup = BeautifulSoup(r.read(), 'html.parser')
    fine = soup.find(text=re.compile('\$'))
    print('Fine: {}'.format(fine))

def logout():
    r = OPENER.open(LOGOUTURL)

if '__main__' == __name__:
    if len(sys.argv) < 2:
        print('Usage: {} username [username ...]'.format(sys.argv[0]))
        sys.exit(1)
    if os.getenv('SCCLPIN'):
        password = os.getenv('SCCLPIN')
    else:
        password = getpass.getpass()
    for username in sys.argv[1:]:
        print('USER: {}'.format(username))
        soup = loginAndReturnSoup(username, password)
        displayCheckedOut(soup)
        fines()
        logout()
