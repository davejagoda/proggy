#!/usr/bin/env python3

import argparse
import pprint
import sys

import boto3


def remove_trailing_dot(s):
    if s.endswith("."):
        return s[:-1]
    return s


def get_domains(r53domains, verbose):
    domains = []
    if verbose > 1:
        print("Number of domains found:{}".format(len(r53domains["Domains"])))
        pprint.pprint(r53domains)
    print("Domain Name          Auto Lock Expiry")
    for domain in r53domains["Domains"]:
        domains.append(domain["DomainName"])
        print(
            "{:20} {} {} {}".format(
                domain["DomainName"],
                domain["AutoRenew"],
                domain["TransferLock"],
                domain["Expiry"],
            )
        )
    return domains


def validate_nameservers(nameservers, verbose):
    results = []
    model_dict = {"Name": "", "GlueIps": ""}
    for nameserver in nameservers:
        assert nameserver.keys() == model_dict.keys()
        assert nameserver["GlueIps"] == []
        if verbose > 1:
            print("nsname:{}".format(nameserver["Name"]))
        results.append(nameserver["Name"])
    return results


def get_domain_details(domain_details, verbose):
    if verbose > 1:
        pprint.pprint(domain_details)
    if verbose > 0:
        print(
            "{:20} {}".format(
                domain_details["DomainName"], domain_details["Nameservers"]
            )
        )
    return validate_nameservers(domain_details["Nameservers"], verbose)


def get_zones(domain_detail, verbose):
    zones = []
    if verbose > 0:
        print("Number of zones found:{}".format(len(domain_detail["HostedZones"])))
    if verbose > 1:
        pprint.pprint(domain_detail)
    for zone in domain_detail["HostedZones"]:
        if verbose > 1:
            print(zone["Name"])
        zones.append((zone["Id"], zone["Name"]))
    return zones


def validate_resource_records(rr, verbose):
    nameservers = []
    model_dict = {"Value": ""}
    for r in rr:
        assert r.keys() == model_dict.keys()
        if verbose > 1:
            print("nsname:{}".format(r["Value"]))
        nameservers.append(remove_trailing_dot(r["Value"]))
    return nameservers


def get_zone_details(zone_detail, verbose):
    if verbose > 1:
        pprint.pprint(zone_detail)
    for rrs in zone_detail["ResourceRecordSets"]:
        if verbose > 0:
            print(
                "{:20} {} {}".format(rrs["Name"], rrs["Type"], rrs["ResourceRecords"])
            )
        if "NS" == rrs["Type"]:
            return validate_resource_records(rrs["ResourceRecords"], verbose)


def find_A_record(zone_detail, verbose):
    if verbose > 1:
        pprint.pprint(zone_detail)
    for rrs in zone_detail["ResourceRecordSets"]:
        if "A" == rrs["Type"]:
            return rrs["ResourceRecords"][0]["Value"]
    return None


def set_nameservers(zone_name, list_of_nameservers, verbose):
    print("fixing nameservers")
    r53domains = boto3.client("route53domains", region_name="us-east-1")
    r53domains.update_domain_nameservers(
        DomainName=zone_name,
        Nameservers=[dict(Name=nameserver) for nameserver in list_of_nameservers],
    )


def create_A_record(zone_name, zone_id, ip_address, verbose):
    print("creating A record")
    r53 = boto3.client("route53", region_name="us-east-1")
    r53.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            "Changes": [
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": "*.{}.".format(zone_name),
                        "Type": "A",
                        "TTL": 300,
                        "ResourceRecords": [{"Value": ip_address}],
                    },
                }
            ]
        },
    )


if "__main__" == __name__:
    domains_hash = {}
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("-a", "--a_record_ip", default=None)
    args = parser.parse_args()
    r53domains = boto3.client("route53domains", region_name="us-east-1")
    domains = get_domains(r53domains.list_domains(), args.verbose)
    for domain in domains:
        assert domain not in domains_hash
        domains_hash[domain] = get_domain_details(
            r53domains.get_domain_detail(DomainName=domain), args.verbose
        )
    r53 = boto3.client("route53", region_name="us-east-1")
    zones = get_zones(r53.list_hosted_zones(), args.verbose)
    for zone_id, zone_name in zones:
        zone_name = remove_trailing_dot(zone_name)
        list_of_nameservers = get_zone_details(
            r53.list_resource_record_sets(HostedZoneId=zone_id), args.verbose
        )
        A_record = find_A_record(
            r53.list_resource_record_sets(HostedZoneId=zone_id), args.verbose
        )
        if args.a_record_ip is not None:
            fix_it = input("create A record Y/N ")
            if "Y" == fix_it:
                create_A_record(zone_name, zone_id, args.a_record_ip, args.verbose)
        else:
            print(A_record)
        if list_of_nameservers == domains_hash[zone_name]:
            print(zone_name + " match")
        else:
            print(
                zone_name
                + " no match: {} {}".format(
                    list_of_nameservers, domains_hash[zone_name]
                )
            )
            fix_it = input("fix nameservers Y/N ")
            if "Y" == fix_it:
                set_nameservers(zone_name, list_of_nameservers, args.verbose)
    if args.verbose > 0:
        pprint.pprint(domains_hash)
