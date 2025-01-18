#!/usr/bin/env python3

import argparse
import json
import os
import sys

import requests


def list_users(headers, verbose):
    url = "https://api.notion.com/v1/users"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        users_data = response.json()
        print(json.dumps(users_data, indent=2))
    else:
        print(f"Error fetching users: {response.status_code}, {response.text}")


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()
    NOTION_API_KEY = os.getenv("NOTION_API_KEY")
    if NOTION_API_KEY is None:
        print("set NOTION_API_KEY environment variable")
        sys.exit(1)
    HEADERS = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }
    list_users(HEADERS, args.verbose)
