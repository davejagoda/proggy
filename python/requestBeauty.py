#!/usr/bin/env python3

# example:
# pipenv run ./requestBeauty.py -s https://sccl.bibliocommons.com/user/login -u USER -p PIN -l Featured
import argparse
import bs4
import requests
import urllib.parse


def getSess(url, username, password, useragent, verbose=0):
    if useragent:
        headers = {"User-Agent": useragent}
    else:
        headers = {"User-Agent": "Mozilla/5.0"}
    data = []
    s = requests.Session()
    r = s.get(url, headers=headers)
    if verbose > 0:
        print("HTTP status_code:{}".format(r.status_code))
        print("HTTP history:{}".format(r.history))
        print("HTTP headers:{}".format(r.headers))
    if verbose > 1:
        print(r.content)
    soup = bs4.BeautifulSoup(r.content, "html5lib")
    if verbose > 1:
        print(soup)
    for f in soup.find_all("form"):
        if f.has_attr("method") and "post" == f["method"]:
            action = f["action"]
            if verbose > 0:
                print("ACTION:", action)
            for c in f.find_all("input"):
                if verbose > 0:
                    print("INPUT:{}".format(c))
                try:
                    value = c["value"]
                except:
                    value = ""
                if verbose > 0:
                    try:
                        print(c["name"], c["type"], value.encode("utf8"))
                    except:
                        print("NO NAME", c["type"], value.encode("utf8"))
                if "text" == c["type"]:
                    value = username
                if "password" == c["type"]:
                    value = password
                try:
                    data.append((c["name"], value))
                except:
                    print("no name exception:{}".format(c))
    return s, action, data


def postSess(s, url, data, loggedInString, useragent, verbose=0):
    if useragent:
        headers = {"User-Agent": useragent}
    else:
        headers = {"User-Agent": "Mozilla/5.0"}
    headers["Referer"] = url
    if verbose > 0:
        print("url:{}".format(url))
        print("headers:{}".format(headers))
        print("data:{}".format(data))
    r = s.post(url, headers=headers, data=data)
    if verbose > 0:
        print("HTTP status_code:{}".format(r.status_code))
        print("HTTP history:{}".format(r.history))
        print("HTTP headers:{}".format(r.headers))
    if verbose > 1:
        print(r.content)
    soup = bs4.BeautifulSoup(r.content, "html5lib")
    return loggedInString in soup.get_text()


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--site", required=True)
    parser.add_argument("-u", "--username", required=True)
    parser.add_argument("-p", "--password", required=True)
    parser.add_argument("-l", "--loggedInString", required=True)
    parser.add_argument("-a", "--userAgentString")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()
    if args.verbose > 0:
        print(args.site, args.username, args.password)
    (s, action, data) = getSess(
        args.site,
        args.username,
        args.password,
        args.userAgentString,
        verbose=args.verbose,
    )
    if args.verbose > 0:
        print(action)
        print(data)
    (scheme, netloc, path, params, query, fragment) = urllib.parse.urlparse(action)
    if "" == scheme:
        (scheme, netloc, path, params, query, fragment) = urllib.parse.urlparse(
            args.site
        )
        action = scheme + "://" + netloc + "/" + action
    if postSess(
        s, action, data, args.loggedInString, args.userAgentString, verbose=args.verbose
    ):
        print("logged in")
    else:
        print("not logged in")
