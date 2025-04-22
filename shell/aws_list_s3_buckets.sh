#!/bin/bash

set -Eeuo pipefail

for bucket in $(aws s3api list-buckets --output text | grep BUCKETS | cut -f 3)
do
    echo $bucket
    aws s3api get-bucket-versioning --bucket $bucket --output text || true
    aws s3api get-public-access-block --bucket $bucket --output text || true
done
