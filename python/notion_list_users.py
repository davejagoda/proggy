#!/usr/bin/env python3

import argparse
import json
import os
import sys

import requests


def get_users(headers, verbose):
    url = "https://api.notion.com/v1/users"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        users = response.json()
        assert set(users.keys()) == set(
            [
                "object",
                "results",
                "next_cursor",
                "has_more",
                "type",
                "user",
                "request_id",
            ]
        )
        assert False == users.get("has_more")
        assert None == users.get("next_cursor")
        assert "list" == users.get("object")
        if verbose > 0:
            print(json.dumps(users, indent=2, sort_keys=True))
        return users.get("results")
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
    users = get_users(HEADERS, args.verbose)
    bots = []
    persons = []
    for user in users:
        if user.get("type") == "bot":
            bots.append(user)
            continue
        if user.get("type") == "person":
            persons.append(user)
            continue
        print("unexpected user type")
        sys.exit(1)
    print("bots")
    print("----")
    for bot in bots:
        print(bot.get("name"))
    print("persons")
    print("-------")
    for person in persons:
        print(person.get("person").get("email"))
