#!/usr/bin/env python3


"""
Remember back when Postman was a boy?
"""

import argparse
import json
import os

import requests

if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--api", required=True, help="Use this API key")
    parser.add_argument("-j", "--json", required=True, help="POST this JSON")
    parser.add_argument("-u", "--url", required=True, help="POST to this URL")
    parser.add_argument(
        "-v", "--verbosity", action="count", default=0, help="verbosity"
    )
    args = parser.parse_args()
    headers = {"Content-Type": "application/json", "x-api-key": args.api}
    with open(args.json) as f:
        data = f.read()
    response = requests.post(url=args.url, headers=headers, data=data)
    print(f"HTTP status: {response.status_code}")
    print(f"HTTP response text: {response.text}")
    if args.verbosity > 1:
        print(json.dumps(response.json(), indent=2, sort_keys=True))
