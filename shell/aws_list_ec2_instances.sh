#!/bin/bash

for region in $(aws ec2 describe-regions | grep RegionName | cut -d '"' -f 4 | sort); do
    echo $region
    for instance in $(aws ec2 describe-instances --region $region | grep InstanceId | cut -d '"' -f 4 | sort); do
        echo -n $instance
        aws ec2 describe-instance-attribute --region $region --instance-id $instance --attribute disableApiTermination | grep Value | cut -d : -f 2
    done
done
