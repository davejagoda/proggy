#!/usr/bin/env python3

# http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python

import argparse
import boto3
import queue
import threading
import aws_lib

def output_region_data(element):
    (region_name, keys, resv, secg) = element
    print(region_name)
    if keys: print(keys)
    if resv: print(resv)
    if secg: print(secg)

def parse_keys_response(response):
    keys = aws_lib.extract_response(response, 'KeyPairs')
    return('\n'.join(['K {} {}'.format(
        k['KeyFingerprint'],
        k['KeyName']) for k in keys]))

def parse_resv_response(response):
    resv = aws_lib.extract_response(response, 'Reservations')
    return('\n'.join(['I {} {} {} {} {}'.format(
        r['Instances'][0]['InstanceId'],
        r['Instances'][0]['ImageId'],
        r['Instances'][0]['InstanceType'],
        r['Instances'][0]['PublicDnsName'],
        r['Instances'][0]['KeyName']) for r in resv]))

def parse_secg_response(response):
    secg = aws_lib.extract_response(response, 'SecurityGroups')
    return('\n'.join(['S {} {} {}'.format(
        s['GroupId'],
        s['GroupName'],
        s['Description']) for s in secg]))

def get_instance_data_from_region(q, region_name):
    session = boto3.session.Session(region_name=region_name)
    ec2 = session.client('ec2')

    keys = parse_keys_response(ec2.describe_key_pairs())
    resv = parse_resv_response(ec2.describe_instances())
    secg = parse_secg_response(ec2.describe_security_groups())

    q.put((region_name, keys, resv, secg))

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--threads', action='store_true',
                        help='use this argument to run multiple threads')
    args = parser.parse_args()
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    q = queue.Queue()
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
