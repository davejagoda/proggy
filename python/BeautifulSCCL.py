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
        j = json.loads(app_json_script.contents[0])
    except:
        print('failed to log in')
        sys.exit(1)
    keys_list = list(j['entities']['accounts'])
    print('Email: {}'.format(
        j['entities']['accounts'][keys_list[0]]['digitalNotificationEmail']))
    results = []
    for value in j['entities']['checkouts'].values():
        results.append('{}:{}'.format(value['dueDate'], value['bibTitle']))
    results.sort()
    if results:
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
    location = parser.add_mutually_exclusive_group()
    location.add_argument('--paloalto', '-p', action='store_true',
                          help='check Palo Alto library instead of SCCL')
    location.add_argument('--sjpl', '-s', action='store_true',
                          help='check San Jose library instead of SCCL')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='be verbose')
    args = parser.parse_args()
    loc = 'sccl'
    if args.paloalto:
        loc = 'paloalto'
    if args.sjpl:
        loc = 'sjpl'
    LOGINURL = 'https://{}.bibliocommons.com/user/login'.format(loc)
    LOGOUTURL = 'https://{}.bibliocommons.com/user/logout'.format(loc)
    CHECKEDOUTURL = 'http://{}.bibliocommons.com/checkedout'.format(loc)
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
