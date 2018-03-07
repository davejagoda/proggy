#!/usr/bin/env python

import argparse
import boto3

def print_bucket_summary(client, bucket_name, verbose):
    print('B {} {}'.format(
        client.get_bucket_location(Bucket=bucket_name)['LocationConstraint'],
        bucket_name
    ))

def print_bucket_contents(s3, bucket_name, verbose):
    bucket = s3.Bucket(bucket_name)
    for item in bucket.objects.all():
        key = item.key
        obj = s3.Object(bucket_name, key)
        if verbose > 0:
            print(u'K {} {} {}'.format(obj.last_modified,
                                      obj.server_side_encryption,
                                      key))
        else:
            print(u'K {} {}'.format(obj.server_side_encryption, key))

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('-b', '--buckets', nargs='*')
    parser.add_argument('-c', '--contents', action='store_true')
    args = parser.parse_args()
    client = boto3.client('s3') # low level client
    s3 = boto3.resource('s3') # high level resource
    if args.buckets:
        bucket_list = args.buckets
    else:
        bucket_list = [bucket.name for bucket in s3.buckets.all()]
    for bucket_name in bucket_list:
        print_bucket_summary(client, bucket_name, args.verbose)
        if args.contents:
            try:
                print_bucket_contents(s3, bucket_name, args.verbose)
            except Exception as e:
                print('Caught exception:{} on bucket:{}'.format(e, bucket_name))
