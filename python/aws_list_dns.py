#!/usr/bin/env python3

import argparse
import boto3
import pprint

def print_domains(r53domains, verbose):
    if verbose > 0:
        print('Number of domains found:{}'.format(len(r53domains['Domains'])))
        pprint.pprint(r53domains)
    print('Domain Name          Auto Lock Expiry')
    for domain in r53domains['Domains']:
        print('{:20} {} {} {}'.format(
            domain['DomainName'],
            domain['AutoRenew'],
            domain['TransferLock'],
            domain['Expiry']))
        if verbose > 0:
            pprint.pprint(domain)

def print_record_sets(r53record_sets, verbose):
    if verbose > 0:
        print('Number of records found:{}'.format(len(r53record_sets['ResourceRecordSets'])))
        pprint.pprint(r53record_sets)
    print('Record Set')
    for record_set in r53record_sets['ResourceRecordSets']:
        print('{:20} {} {} {}'.format(
            record_set['Name'],
            record_set['ResourceRecords'],
            record_set['TTL'],
            record_set['Type']))

def print_zones(zones, verbose):
    print('ZONES')
    if verbose > 0:
        print('Number of zones found:{}'.format(len(zones['HostedZones'])))
        pprint.pprint(zones)
    for zone in zones['HostedZones']:
        print('{:20} {} {}'.format(
            zone['Name'],
            zone['Id'],
            zone['ResourceRecordSetCount']))
        response = boto3.client('route53', region_name='us-east-1')
        print_record_sets(response.list_resource_record_sets(
            HostedZoneId=zone['Id']), args.verbose)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('-z', '--zone')
    args = parser.parse_args()
    response = boto3.client('route53domains', region_name='us-east-1')
    print_domains(response.list_domains(), args.verbose)
    response = boto3.client('route53', region_name='us-east-1')
    print_zones(response.list_hosted_zones(), args.verbose)
