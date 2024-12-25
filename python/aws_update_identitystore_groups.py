#!/usr/bin/env python3

import argparse
import boto3
import os
import sys
from botocore.exceptions import ClientError

def get_group_by_name(identitystore_id, group, region, verbose):
    client = boto3.client('identitystore', region_name=region)
    try:
        response = client.get_group_id(
            IdentityStoreId=identitystore_id,
            AlternateIdentifier={
                'UniqueAttribute': {
                    'AttributePath': 'displayName',
                    'AttributeValue': group
                }
            }
        )
        return response['GroupId']
    except ClientError as e:
        print(f'An error occurred: {e}')
        return None

def get_user_by_name(identitystore_id, user, region, verbose):
    client = boto3.client('identitystore', region_name=region)
    try:
        response = client.get_user_id(
            IdentityStoreId=identitystore_id,
            AlternateIdentifier={
                'UniqueAttribute': {
                    'AttributePath': 'userName',
                    'AttributeValue': user
                }
            }
        )
        return response['UserId']
    except ClientError as e:
        print(f'An error occurred: {e}')
        return None

def add_user_to_group(identitystore_id, user_id, group_id, region, verbose):
    client = boto3.client('identitystore', region_name=region)
    try:
        response = client.create_group_membership(
            IdentityStoreId=identitystore_id,
            GroupId=group_id,
            MemberId={
                'UserId': user_id
            }
        )
        return response['ResponseMetadata']['HTTPStatusCode']
    except ClientError as e:
        print(f'An error occurred: {e}')
        return None

def del_user_from_group(identitystore_id, user_id, group_id, region, verbose):
    client = boto3.client('identitystore', region_name=region)
    try:
        response = client.get_group_membership_id(
            IdentityStoreId=identitystore_id,
            GroupId=group_id,
            MemberId={
                'UserId': user_id
            }
        )
        membership_id = response['MembershipId']
    except ClientError as e:
        print(f'An error occurred: {e}')
        return None
    try:
        response = client.delete_group_membership(
            IdentityStoreId=identitystore_id,
            MembershipId=membership_id
        )
        return response['ResponseMetadata']['HTTPStatusCode']
    except ClientError as e:
        print(f'An error occurred: {e}')
        return None

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('-i', '--identitystore_id',
                        default=os.getenv('AWS_IDENTITYSTORE_ID'))
    parser.add_argument('-r', '--region',
                        default=os.getenv('AWS_REGION'))
    parser.add_argument('-a', '--action', choices=['add', 'del'], default='add')
    parser.add_argument('-g', '--group', required=True)
    parser.add_argument('-u', '--user', required=True)
    args = parser.parse_args()
    if args.identitystore_id == None:
        print('provide --identitystore_id argument or set AWS_IDENTITYSTORE_ID')
        sys.exit(1)
    if args.region == None:
        print('provide --region argument or set AWS_REGION')
        sys.exit(1)
    group_id = get_group_by_name(
        args.identitystore_id, args.group, args.region, args.verbose)
    user_id = get_user_by_name(
        args.identitystore_id, args.user, args.region, args.verbose)
    if args.verbose > 0:
        print(group_id, user_id)
    if args.action == 'add':
        print(add_user_to_group(
            args.identitystore_id, user_id, group_id, args.region, args.verbose
        ))
    if args.action == 'del':
        print(del_user_from_group(
            args.identitystore_id, user_id, group_id, args.region, args.verbose
        ))
