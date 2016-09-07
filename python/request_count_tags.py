#!/usr/bin/env python

import argparse
import bs4
import requests

def getSess(url, tag, verbose=0):
    r = requests.get(url)
    if verbose > 0:
        print('HTTP status_code:{}'.format(r.status_code))
        print('HTTP history:{}'.format(r.history))
        print('HTTP headers:{}'.format(r.headers))
    if verbose > 1:
        print(r.content)
    soup = bs4.BeautifulSoup(r.content, 'html5lib')
    if verbose > 1:
        print(soup)
    num_tags = 0
    for f in soup.find_all(tag):
        if verbose > 0:
            print('tag:{}'.format(f))
        num_tags += 1
    return(num_tags)


if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True)
    parser.add_argument('-t', '--tag', required=True)
    parser.add_argument('-v', '--verbose', action='count')
    args = parser.parse_args()
    if args.verbose > 0:
        print(args.url, args.tag)
    print('number of tags of type:{} is {}'.format(args.tag,
        getSess(args.url, args.tag, verbose=args.verbose)))
