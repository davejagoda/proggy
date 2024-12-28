#!/usr/bin/env python3

import argparse
import boto3
import os
import sys
from botocore.exceptions import ClientError


def list_identitystore_users(identitystore_id, region, verbose):
    client = boto3.client("identitystore", region_name=region)
    users = []
    next_token = None
    try:
        while True:
            if next_token:
                response = client.list_users(
                    IdentityStoreId=identitystore_id, NextToken=next_token
                )
            else:
                response = client.list_users(IdentityStoreId=identitystore_id)
            users.extend(response.get("Users", []))
            next_token = response.get("NextToken", None)
            if not next_token:
                break
    except ClientError as e:
        print(f"An error occurred: {e}")
        return []
    return users


def list_identitystore_groups(identitystore_id, region, verbose):
    client = boto3.client("identitystore", region_name=region)
    groups = []
    next_token = None
    try:
        while True:
            if next_token:
                response = client.list_groups(
                    IdentityStoreId=identitystore_id, NextToken=next_token
                )
            else:
                response = client.list_groups(IdentityStoreId=identitystore_id)
            groups.extend(response.get("Groups", []))
            next_token = response.get("NextToken", None)
            if not next_token:
                break
    except ClientError as e:
        print(f"An error occurred: {e}")
        return []
    return groups


def expand_identitystore_group(identitystore_id, group_id, region, verbose):
    client = boto3.client("identitystore", region_name=region)
    members = []
    next_token = None
    try:
        while True:
            if next_token:
                response = client.list_group_memberships(
                    IdentityStoreId=identitystore_id,
                    GroupId=group_id,
                    NextToken=next_token,
                )
            else:
                response = client.list_group_memberships(
                    IdentityStoreId=identitystore_id, GroupId=group_id
                )
            members.extend(response.get("GroupMemberships", []))
            next_token = response.get("NextToken", None)
            if not next_token:
                break
    except ClientError as e:
        print(f"An error occurred: {e}")
        return []
    return members


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument(
        "-i", "--identitystore_id", default=os.getenv("AWS_IDENTITYSTORE_ID")
    )
    parser.add_argument("-r", "--region", default=os.getenv("AWS_REGION"))
    parser.add_argument("-e", "--expand", action="store_true")
    args = parser.parse_args()
    if args.identitystore_id == None:
        print("provide --identitystore_id argument or set AWS_IDENTITYSTORE_ID")
        sys.exit(1)
    if args.region == None:
        print("provide --region argument or set AWS_REGION")
        sys.exit(1)
    user_dict = {}
    users = list_identitystore_users(args.identitystore_id, args.region, args.verbose)
    if users:
        if args.verbose > 0:
            print(f"Found {len(users)} users:")
        for user in users:
            user_id = user["UserId"]
            user_name = user["UserName"]
            if args.verbose > 0:
                print(f"{user_id}: {user_name}")
            assert user_id not in user_dict
            user_dict[user_id] = user_name

    groups = list_identitystore_groups(args.identitystore_id, args.region, args.verbose)
    if groups:
        if args.verbose > 0:
            print(f"Found {len(groups)} groups:")
        for group in sorted(groups, key=lambda d: d["DisplayName"]):
            group_id = group["GroupId"]
            group_name = group["DisplayName"]
            print(f"{group_id}: {group_name}")
            if args.expand:
                members = expand_identitystore_group(
                    args.identitystore_id, group_id, args.region, args.verbose
                )
                if args.verbose > 0:
                    print(f"Found {len(members)} members:")
                output = []
                for member in members:
                    user_id = member["MemberId"]["UserId"]
                    if args.verbose > 0:
                        user_id
                    output.append(user_dict[user_id])
                print("\n".join(sorted(output)))
    else:
        if args.verbose > 0:
            print("No groups found.")
