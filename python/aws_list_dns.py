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

def print_zones(response, verbose):
    print('ZONES')
    if verbose > 0:
        print('Number of zones found:{}'.format(len(response['HostedZones'])))
        pprint.pprint(response)
    for zone in response['HostedZones']:
        print(zone['Name'])

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('-z', '--zone')
    args = parser.parse_args()
    response = boto3.client('route53domains', region_name='us-east-1')
    print_domains(response.list_domains(), args.verbose)
    response = boto3.client('route53', region_name='us-east-1')
    print_zones(response.list_hosted_zones(), args.verbose)
