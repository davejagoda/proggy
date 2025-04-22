#!/bin/bash

set -Eeuo pipefail

for bucket in $(aws s3api list-buckets --output text | grep BUCKETS | cut -f 3)
do
    echo $bucket
    aws s3api put-public-access-block --bucket $bucket --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
done
