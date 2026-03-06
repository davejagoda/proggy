#!/usr/bin/env python3

# this prints out checked out books from SCCL

import argparse
import getpass
import json
import os
import sys
import time
import urllib

from bs4 import BeautifulSoup

OPENER = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())


def loginAndReturnSoup(u, p, verbose=False):
    values = {"name": u, "user_pin": p}
    data = urllib.parse.urlencode(values).encode("utf-8")

    r = OPENER.open(LOGINURL, data)
    r = OPENER.open(CHECKEDOUTURL)
    soup = BeautifulSoup(r.read(), "html.parser")
    if verbose:
        print(soup.prettify())
    return soup


def convertDateFromAmericanTo8601(s, verbose=False):
    if verbose:
        print(s)
    return time.strftime("%Y-%m-%d", time.strptime(s, "%b %d, %Y"))


def displayCheckedOut(soup, verbose=False):
    # find this in the soup:
    # 'script data-iso-key="_0" type="application/json">'
    app_json_script = soup.find("script", {"type": "application/json"})
    try:
        j = json.loads(app_json_script.contents[0])
    except:
        print("failed to log in")
        sys.exit(1)
    keys_list = list(j["entities"]["accounts"])
    print(
        f"Email: {j['entities']['accounts'][keys_list[0]]['digitalNotificationEmail']}"
    )
    results = []
    for value in j["entities"]["checkouts"].values():
        results.append(f"{value['dueDate']}:{value['bibTitle']}")
    results.sort()
    if results:
        print(os.linesep.join(results))


def fines(soup, verbose=False):
    # find this in the soup:
    # <span class="cp-dollar-amount" data-reactid="144">
    fine = soup.find("span", {"class": "cp-dollar-amount"})
    print(f"Fine: {fine.get_text()}")


def logout():
    try:
        r = OPENER.open(LOGOUTURL)
    except urllib.error.HTTPError as e:
        print("got an exception while logging out")
        """
        print(e.getcode)
        print(e.geturl)
        print(e.hdrs)
        print(e.headers)
        print(e.info)
        print(e.msg)
        print(e.name)
        print(e.reason)
        print(e.status)
        print(e.strerror)
        print(e.url)
        print(e.with_traceback)
        """


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("usernames", nargs="+", help="username[s]")
    location = parser.add_mutually_exclusive_group(required=True)
    location.add_argument(
        "--paloalto",
        action="store_true",
        help="check Palo Alto library",
    )
    location.add_argument(
        "--sccl",
        action="store_true",
        help="check Santa Clara County library",
    )
    location.add_argument(
        "--sjpl",
        action="store_true",
        help="check San Jose library",
    )
    location.add_argument(
        "--sunnyvale",
        action="store_true",
        help="check Sunnyvale library",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="be verbose")
    args = parser.parse_args()
    for k, v in vars(args).items():
        if v is True:
            loc = k
    LOGINURL = f"https://{loc}.bibliocommons.com/user/login"
    LOGOUTURL = f"https://{loc}.bibliocommons.com/user/logout"
    CHECKEDOUTURL = f"http://{loc}.bibliocommons.com/checkedout"
    if os.getenv("SCCLPIN"):
        password = os.getenv("SCCLPIN")
    else:
        password = getpass.getpass()
    for username in args.usernames:
        print(f"USER: {username} LOC: {loc}")
        soup = loginAndReturnSoup(username, password, args.verbose)
        displayCheckedOut(soup, args.verbose)
        fines(soup, args.verbose)
        logout()
