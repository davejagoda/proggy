#!/usr/bin/env python3

"""
Remember back when Postman was a boy?
uv run postboy.py
"""

import argparse
import json
import os

import requests

if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--api", default=None, help="Use this API key")
    parser.add_argument("-j", "--json", required=True, help="POST this JSON")
    parser.add_argument(
        "-r", "--redirect", default=False, action="store_true", help="Follow redirects"
    )
    parser.add_argument("-u", "--url", required=True, help="POST to this URL")
    parser.add_argument(
        "-v", "--verbosity", action="count", default=0, help="verbosity"
    )
    args = parser.parse_args()
    headers = {"Content-Type": "application/json"}
    if args.api:
        headers["x-api-key"] = args.api
    if args.verbosity > 1:
        print(headers)
    with open(args.json) as f:
        data = f.read()
    response = requests.post(
        url=args.url, headers=headers, data=data, allow_redirects=args.redirect
    )
    if response.history:
        for item in response.history:
            print(item.status_code, item.url)
    print(f"HTTP status: {response.status_code}")
    print(f"HTTP response text: {response.text}")
    if args.verbosity > 0:
        try:
            print(json.dumps(response.json(), indent=2, sort_keys=True))
        except requests.JSONDecodeError:
            print("Could not decode the response text into json")
