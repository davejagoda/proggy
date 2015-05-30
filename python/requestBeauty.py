#!/usr/bin/env python

import argparse, requests, bs4, re

def getSess(url, username, password, verbose=False):
    data=[]
    s = requests.Session()
    r = s.get(url)
    if verbose:
        print(r.status_code)
        print(r.content)
    soup = bs4.BeautifulSoup(r.content)
    if verbose:
        print(soup)
    for f in soup.find_all('form'):
        if 'post' == f['method']:
            action = f['action']
            if verbose:
                print('ACTION:',f['action'])
            for c in f.find_all('input'):
                try:
                    value = c['value']
                except:
                    value = ''
                if verbose:
                    print(c['name'],c['type'], value.encode('utf8'))
                if 'text' == c['type']:
                    value = username
                if 'password' == c['type']:
                    value = password
                data.append((c['name'],value))
    return(s, action, data)

def postSess(s, url, data, loggedInString, verbose=False):
    r = s.post(url, data=data)
    if verbose:
        print(r.status_code)
        print(r.content)
    soup = bs4.BeautifulSoup(r.content)
    return(soup.find(text=re.compile(loggedInString)) is not None)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--site', required=True)
    parser.add_argument('-u', '--username', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('-l', '--loggedInString', required=True)
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    if args.verbose:
        print(args.site, args.username, args.password)
    (s, action, data) = getSess(args.site, args.username, args.password, verbose=args.verbose)
    if args.verbose:
        print(action)
        print(data)
    if (postSess(s, action, data, args.loggedInString, verbose=args.verbose)):
        print('logged in')
    else:
        print('not logged in')
