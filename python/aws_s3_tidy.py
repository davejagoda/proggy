#!/usr/bin/env python3

# offer to delete empty buckets
# offer to delete empty files
# offer to delete .DS_Store files

import argparse

import boto3
from botocore.exceptions import ClientError


def delete_bucket(client, bucket_name):
    pass


def get_bucket_summary(client, bucket_name, fix):
    bucket_location = client.get_bucket_location(Bucket=bucket_name)[
        "LocationConstraint"
    ]
    # When the bucket's region is US East (N. Virginia),
    # Amazon S3 returns an empty string for the bucket's region
    if None == bucket_location:
        bucket_location = "us-east-1"
    return "B {} {}".format(bucket_location, bucket_name)


def walk_bucket_objects(bucket_name, fix):
    bucket = s3.Bucket(bucket_name)
    count = 0
    for obj in bucket.objects.all():
        count += 1
        if obj.key.endswith(".DS_Store") or 0 == obj.size:
            if fix and "y" == input(
                "delete object {} with size {} ".format(obj.key, obj.size)
            ):
                print(obj.delete())
            else:
                print("{} {}".format(obj.key, obj.size))
    return count


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--buckets", nargs="*")
    parser.add_argument("-f", "--fix", action="store_true")
    args = parser.parse_args()
    client = boto3.client("s3")  # low level client
    s3 = boto3.resource("s3")  # high level resource
    if args.buckets:
        bucket_list = args.buckets
    else:
        bucket_list = [bucket.name for bucket in s3.buckets.all()]
    for bucket_name in bucket_list:
        summary = get_bucket_summary(client, bucket_name, args.fix)
        count = walk_bucket_objects(bucket_name, args.fix)
        print("{:>5}#{}".format(count, summary))
        if 0 == count:
            if args.fix:
                print(client.delete_bucket(Bucket=bucket_name))
            else:
                print("empty bucket")
