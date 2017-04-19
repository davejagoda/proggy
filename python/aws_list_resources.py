#!/usr/bin/env python

import boto3
import pprint

def get_instance_data_from_region(region_name):
    ec2 = boto3.client('ec2', region_name=region_name)
    response = ec2.describe_instances()
    assert(2 == len(response))
    for resource in response:
        if 'ResponseMetadata' != resource:
            assert('Reservations' == resource)
            if 0 == len(response[resource]):
                print('{}:{}'.format(region_name, 'None'))
            else:
                print(region_name)
                assert(list == type(response[resource]))
                for item in response[resource]:
                    pprint.pprint(item)

if '__main__' == __name__:
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    for region in response['Regions']:
        assert(2 == len(region))
        region_name = region['RegionName']
        assert('ec2.{}.amazonaws.com'.format(region_name) == region['Endpoint'])
        get_instance_data_from_region(region_name)
