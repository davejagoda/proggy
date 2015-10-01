#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this prints out checked out books from SCCL

from bs4 import BeautifulSoup
import sys, os, getpass, urllib, urllib2, re, time, argparse

LOGINURL = 'https://sccl.bibliocommons.com/user/login'
LOGOUTURL = 'https://sccl.bibliocommons.com/user/logout'
CHECKEDOUTURL = 'http://sccl.bibliocommons.com/checkedout?display_quantity=25'
FINESURL = 'https://sccl.bibliocommons.com/fines'
OPENER = urllib2.build_opener(urllib2.HTTPCookieProcessor())

def loginAndReturnSoup(u, p, verbose=False):
    values = { 'name' : u,
               'user_pin' : p }
    data = urllib.urlencode(values)
    r = OPENER.open(LOGINURL, data)
    r = OPENER.open(CHECKEDOUTURL)
    soup = BeautifulSoup(r.read(), 'html.parser')
    if verbose: print(soup.prettify().encode('utf8'))
    logged_in_user = soup.find(text=re.compile('Logged in as '))
    try:
        print('User: {}'.format(logged_in_user))
    except:
        print('Bad password')
        sys.exit(1)
    return(soup)

def convertDateFromAmericanTo8601(s):
    return(time.strftime('%Y-%m-%d', time.strptime(s, '%b %d, %Y')))

def displayCheckedOut(soup, verbose=False):
#   <a class="jacketCoverLink" href="/item/show/973973016_office_space" target="_parent" title="Office Space">
    titles = []
    duedates = []
    for tt in soup.find_all('a', 'jacketCoverLink'):
        title = None
        for kid in tt.children:
# find the title of the child, if there's more than one child use the last one
            title = kid['title'].encode('utf8')
            if verbose: print(title)
            titles.append(title)
# 2015-10-01 <span class="checkedout_status out">
    for dd in soup.find_all('span', 'checkedout_status'):
        duedate = convertDateFromAmericanTo8601(dd.text.strip())
        duedates.append(duedate)
    for i in xrange(len(titles)):
        print('UNIT: {} {}'.format(duedates[i], titles[i]))
    assert len(duedates) == len(titles)

def fines():
    r = OPENER.open(FINESURL)
    soup = BeautifulSoup(r.read(), 'html.parser')
    fine = soup.find(text=re.compile('\$'))
    print('Fine: {}'.format(fine))

def logout():
    r = OPENER.open(LOGOUTURL)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('usernames', nargs='+', help='username[s]')
    parser.add_argument('--verbose', '-v', action='store_true', help='be verbose')
    args = parser.parse_args()
    if os.getenv('SCCLPIN'):
        password = os.getenv('SCCLPIN')
    else:
        password = getpass.getpass()
    for username in args.usernames:
        print('USER: {}'.format(username))
        soup = loginAndReturnSoup(username, password, args.verbose)
        displayCheckedOut(soup, args.verbose)
        fines()
        logout()
