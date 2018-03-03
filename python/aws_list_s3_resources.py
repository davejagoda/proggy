#!/usr/bin/env python

import argparse
import boto3

def print_bucket_contents(s3, bucket_name, verbose):
    print('B {}'.format(bucket_name))
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
    parser.add_argument('-b', '--bucket')
    args = parser.parse_args()
    s3 = boto3.resource('s3')
    if args.bucket:
        print_bucket_contents(s3, args.bucket, args.verbose)
    else:
        for bucket in s3.buckets.all():
            bucket_name = bucket.name
            print_bucket_contents(s3, bucket_name, args.verbose)
