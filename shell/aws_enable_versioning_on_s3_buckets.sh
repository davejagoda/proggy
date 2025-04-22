#!/bin/bash

set -Eeuo pipefail

for bucket in $(aws s3api list-buckets --output text | grep BUCKETS | cut -f 3)
do
    echo $bucket
    aws s3api put-bucket-versioning --bucket $bucket --versioning-configuration Status=Enabled
done
