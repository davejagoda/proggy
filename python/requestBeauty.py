#!/usr/bin/env python

# examples:
# ./requestBeauty.py -s https://sccl.bibliocommons.com/user/login -u <USERNAME> -p <PIN> -l 'Logged in as '
# ./requestBeauty.py -s https://stormy-escarpment-6340.herokuapp.com/admin -u <USERNAME> -p <PASSWORD> -l 'Welcome'
import argparse, requests, bs4, re, urlparse

def getSess(url, username, password, useragent, verbose=False):
    if useragent:
        headers = {'User-Agent': useragent}
    else:
        headers = {'User-Agent': 'Mozilla/5.0'}
    data=[]
    s = requests.Session()
    r = s.get(url, headers=headers)
    if verbose:
        print(r.status_code)
        print(r.headers)
        print(r.content)
    soup = bs4.BeautifulSoup(r.content)
    if verbose:
        print(soup)
    for f in soup.find_all('form'):
        if 'post' == f['method']:
            action = f['action']
            if verbose:
                print('ACTION:',action)
            for c in f.find_all('input'):
                try:
                    value = c['value']
                except:
                    value = ''
                if verbose:
                    try:
                        print(c['name'],c['type'], value.encode('utf8'))
                    except:
                        print('NO NAME',c['type'], value.encode('utf8'))
                if 'text' == c['type']:
                    value = username
                if 'password' == c['type']:
                    value = password
                try:
                    data.append((c['name'],value))
                except:
                    print('no name exception:{}'.format(c))
    return(s, action, data)

def postSess(s, url, data, loggedInString, useragent, verbose=False):
    if useragent:
        headers = {'User-Agent': useragent}
    else:
        headers = {'User-Agent': 'Mozilla/5.0'}
    headers['Referer'] = url
    if verbose:
        print('url:{}'.format(url))
        print('headers:{}'.format(headers))
        print('data:{}'.format(data))
    r = s.post(url, headers=headers, data=data)
    if verbose:
        print(r.status_code)
        print(r.headers)
        print(r.content)
    soup = bs4.BeautifulSoup(r.content)
    return(soup.find(text=re.compile(loggedInString)) is not None)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--site', required=True)
    parser.add_argument('-u', '--username', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('-l', '--loggedInString', required=True)
    parser.add_argument('-a', '--userAgentString')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    if args.verbose:
        print(args.site, args.username, args.password)
    (s, action, data) = getSess(args.site, args.username, args.password, args.userAgentString, verbose=args.verbose)
    if args.verbose:
        print(action)
        print(data)
    (scheme, netloc, path, params, query, fragment) = urlparse.urlparse(action)
    if '' == scheme:
        (scheme, netloc, path, params, query, fragment) = urlparse.urlparse(args.site)
        action = scheme + '://' + netloc + '/' + action
    if postSess(s, action, data, args.loggedInString, args.userAgentString, verbose=args.verbose):
        print('logged in')
    else:
        print('not logged in')
