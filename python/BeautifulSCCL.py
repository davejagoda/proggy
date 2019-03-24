#!/usr/bin/env python3

# this prints out checked out books from SCCL

from bs4 import BeautifulSoup
import argparse
import getpass
import json
import os
import sys
import time
import urllib

LOGINURL = 'https://sccl.bibliocommons.com/user/login'
LOGOUTURL = 'https://sccl.bibliocommons.com/user/logout'
CHECKEDOUTURL = 'http://sccl.bibliocommons.com/checkedout?display_quantity=25'
OPENER = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())

def loginAndReturnSoup(u, p, verbose=False):
    values = { 'name' : u,
               'user_pin' : p }
    data = urllib.parse.urlencode(values).encode('utf-8')

    r = OPENER.open(LOGINURL, data)
    r = OPENER.open(CHECKEDOUTURL)
    soup = BeautifulSoup(r.read(), 'html.parser')
    if verbose: print(soup.prettify())
    return(soup)

def convertDateFromAmericanTo8601(s, verbose=False):
    if verbose: print(s)
    return(time.strftime('%Y-%m-%d', time.strptime(s, '%b %d, %Y')))

def displayCheckedOut(soup, verbose=False):
    # find this in the soup:
    # 'script data-iso-key="_0" type="application/json">'
    app_json_script = soup.find('script', {'type': 'application/json'})
    try:
        j = json.loads(app_json_script.get_text())
    except:
        print('failed to log in')
        sys.exit(1)
    print('Email: {}'.format(
        j['entities']['accounts']['69905905']['digitalNotificationEmail']))
    results = []
    for value in j['entities']['checkouts'].values():
        results.append('{}:{}'.format(value['dueDate'], value['bibTitle']))
    results.sort()
    print(os.linesep.join(results))

def fines(soup, verbose=False):
    # find this in the soup:
    # <span class="cp-dollar-amount" data-reactid="144">
    fine = soup.find('span', {'class': 'cp-dollar-amount'})
    print('Fine: {}'.format(fine.get_text()))

def logout():
    r = OPENER.open(LOGOUTURL)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('usernames', nargs='+', help='username[s]')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='be verbose')
    args = parser.parse_args()
    if os.getenv('SCCLPIN'):
        password = os.getenv('SCCLPIN')
    else:
        password = getpass.getpass()
    for username in args.usernames:
        print('USER: {}'.format(username))
        soup = loginAndReturnSoup(username, password, args.verbose)
        displayCheckedOut(soup, args.verbose)
        fines(soup, args.verbose)
        logout()
