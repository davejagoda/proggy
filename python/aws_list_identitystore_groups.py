#!/usr/bin/env python3

import argparse
import boto3
import os
import sys
from botocore.exceptions import ClientError

def list_identitystore_groups(identitystore_id, region, verbose):
    client = boto3.client('identitystore', region_name=region)
    groups = []
    next_token = None
    try:
        while True:
            if next_token:
                response = client.list_groups(
                    IdentityStoreId=identitystore_id,
                    NextToken=next_token
                )
            else:
                response = client.list_groups(IdentityStoreId=identitystore_id)
            groups.extend(response.get('Groups', []))
            next_token = response.get('NextToken', None)
            if not next_token:
                break
    except ClientError as e:
        print(f'An error occurred: {e}')
        return []
    return groups

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('-i', '--identitystore_id',
                        default=os.getenv('AWS_IDENTITYSTORE_ID'))
    parser.add_argument('-r', '--region',
                        default=os.getenv('AWS_REGION'))
    args = parser.parse_args()
    if args.identitystore_id == None:
        print('provide --identitystore_id argument or set AWS_IDENTITYSTORE_ID')
        sys.exit(1)
    if args.region == None:
        print('provide --region argument or set AWS_REGION')
        sys.exit(1)
    groups = list_identitystore_groups(args.identitystore_id,
                                       args.region,
                                       args.verbose)
    if groups:
        if args.verbose > 0:
            print(f'Found {len(groups)} groups:')
        for group in groups:
            print(f'{group["GroupId"]} {group["DisplayName"]}')
    else:
        if args.verbose > 0:
            print('No groups found.')
