#!/usr/bin/env python

# http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python

import argparse
import boto3
import pprint
import Queue
import threading

def output_region_data(element):
    (region_name, resources) = element
    if 0 == len(resources):
        print('{}:{}'.format(region_name, 'None'))
    else:
        print(region_name)
        for item in resources:
            pprint.pprint(item)

def get_instance_data_from_region(q, region_name):
    session = boto3.session.Session(region_name=region_name)
    ec2 = session.client('ec2')
    response = ec2.describe_instances()
    assert(2 == len(response))
    for resource in response:
        if 'ResponseMetadata' != resource:
            assert('Reservations' == resource)
            assert(list == type(response[resource]))
            q.put((region_name, response[resource]))
    return

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--threads', action='store_true',
                        help='use this argument to run mutiple threads')
    args = parser.parse_args()
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    q = Queue.Queue()
    thread_list = []
    for region in response['Regions']:
        assert(2 == len(region))
        region_name = region['RegionName']
        assert('ec2.{}.amazonaws.com'.format(region_name) ==
               region['Endpoint'])
        if args.threads:
            thread_list.append(threading.Thread(target=
                                                get_instance_data_from_region,
                                                args=(q, region_name)))
        else:
            get_instance_data_from_region(q, region_name)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    while not q.empty():
        output_region_data(q.get())
