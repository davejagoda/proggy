#!/usr/bin/env python

# http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python

import argparse
import boto3
import Queue
import threading

def output_region_data(element):
    (region_name, secg, vpc) = element
    print(region_name)
    if secg: print(secg)
    if vpc: print(vpc)

def extract_response(response, response_type):
    assert(2 == len(response))
    assert(200 == response['ResponseMetadata']['HTTPStatusCode'])
    results = response[response_type]
    assert(list == type(results))
    return(results)

def parse_secg_response(response):
    secg = extract_response(response, 'SecurityGroups')
    return('\n'.join(['S {} {} {}'.format(s['GroupId'],
                                          s['GroupName'],
                                          s['Description']) for s in secg if 'VpcId' not in s]))

def parse_vpc_response(response):
    vpc = extract_response(response, 'Vpcs')
    return('\n'.join(['V {}'.format(v['VpcId']) for v in vpc if not v['IsDefault']]))

def get_instance_data_from_region(q, region_name):
    session = boto3.session.Session(region_name=region_name)
    ec2 = session.client('ec2')

    secg = parse_secg_response(ec2.describe_security_groups())
    vpc = parse_vpc_response(ec2.describe_vpcs())
    q.put((region_name, secg, vpc))

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
