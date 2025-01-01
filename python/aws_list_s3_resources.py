#!/usr/bin/env python3

import argparse

import boto3
from botocore.exceptions import ClientError


def print_bucket_acl(client, bucket_name, verbose):
    response = client.get_bucket_acl(Bucket=bucket_name)
    assert 3 == len(response)
    assert 200 == response["ResponseMetadata"]["HTTPStatusCode"]
    print(response["Owner"])
    print(response["Grants"])


def print_bucket_policy(client, bucket_name, verbose):
    try:
        response = client.get_bucket_policy(Bucket=bucket_name)
        assert 2 == len(response)
        assert 200 == response["ResponseMetadata"]["HTTPStatusCode"]
        print(response["Policy"])
    except ClientError as e:
        if e.response["Error"]["Code"] == "NoSuchBucketPolicy":
            print("No policies set on this bucket")
        else:
            print("Caught exception:{} on bucket:{}".format(e, bucket_name))


def print_bucket_summary(client, bucket_name, verbose):
    bucket_location = client.get_bucket_location(Bucket=bucket_name)[
        "LocationConstraint"
    ]
    # When the bucket's region is US East (N. Virginia),
    # Amazon S3 returns an empty string for the bucket's region
    if None == bucket_location:
        bucket_location = "us-east-1"
    print("B {} {}".format(bucket_location, bucket_name))


def print_bucket_contents(s3, bucket_name, verbose):
    bucket = s3.Bucket(bucket_name)
    for item in bucket.objects.all():
        key = item.key
        obj = s3.Object(bucket_name, key)
        if verbose > 0:
            print(
                "K {} {} {}".format(obj.last_modified, obj.server_side_encryption, key)
            )
        else:
            print("K {} {}".format(obj.server_side_encryption, key))


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--buckets", nargs="*")
    parser.add_argument("-a", "--acl", action="store_true")
    parser.add_argument("-c", "--contents", action="store_true")
    parser.add_argument("-p", "--policy", action="store_true")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()
    client = boto3.client("s3")  # low level client
    s3 = boto3.resource("s3")  # high level resource
    if args.buckets:
        bucket_list = args.buckets
    else:
        bucket_list = [bucket.name for bucket in s3.buckets.all()]
    for bucket_name in bucket_list:
        print_bucket_summary(client, bucket_name, args.verbose)
        if args.policy:
            print_bucket_policy(client, bucket_name, args.verbose)
        if args.acl:
            print_bucket_acl(client, bucket_name, args.verbose)
        if args.contents:
            try:
                print_bucket_contents(s3, bucket_name, args.verbose)
            except Exception as e:
                print("Caught exception:{} on bucket:{}".format(e, bucket_name))
