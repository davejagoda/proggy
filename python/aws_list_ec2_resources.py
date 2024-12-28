#!/usr/bin/env python3

# http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python

COP = chr(0x1F46E)
BOMB = chr(0x1F4A3)
KEY = chr(0x1F511)
DISK = chr(0x1F4BE)

import argparse
import boto3
import queue
import threading
import aws_lib


def print_results(results):
    for result in results:
        print(" ".join(result))


def output_region_data(element):
    (region_name, keyp, resv, vols, neti, elip, secg, vpcs) = element
    print(region_name)
    if keyp:
        print_results(keyp)
    if resv:
        print_results(resv)
    if vols:
        print_results(vols)
    if neti:
        print_results(neti)
    if elip:
        print_results(elip)
    if secg:
        print_results(secg)
    if vpcs:
        print_results(vpcs)


def is_API_termination_disabled(ec2, instance_id):
    if ec2.describe_instance_attribute(
        InstanceId=instance_id, Attribute="disableApiTermination"
    )["DisableApiTermination"]["Value"]:
        return COP
    else:
        return BOMB


def parse_keyp_response(response):
    # results is a list of tuples
    results = []
    keyp = aws_lib.extract_response(response, "KeyPairs")
    for k in keyp:
        results.append(("K", KEY, k["KeyFingerprint"], k["KeyName"]))
    return results


def process_and_parse_resv_response(ec2, response):
    # results is a list of tuples
    results = []
    resv = aws_lib.extract_response(response, "Reservations")
    for r in resv:
        instances = r.get("Instances")
        assert 1 == len(instances)
        instance = instances[0]
        results.append(
            (
                "I",
                is_API_termination_disabled(ec2, instance.get("InstanceId")),
                instance.get("InstanceId"),
                instance.get("ImageId"),
                instance.get("InstanceType"),
                instance.get("PublicDnsName"),
                instance.get("KeyName"),
            )
        )
    return results


def parse_vols_response(response):
    # results is a list of tuples
    results = []
    vols = aws_lib.extract_response(response, "Volumes")
    for v in vols:
        results.append(
            ("V", DISK, v["VolumeId"], "{}GB".format(v["Size"]), v["VolumeType"])
        )
    return results


def parse_neti_response(response):
    # results is a list of tuples
    results = []
    neti = aws_lib.extract_response(response, "NetworkInterfaces")
    for n in neti:
        results.append(("N", n["NetworkInterfaceId"], n["PrivateIpAddress"]))
    return results


def parse_elip_response(response):
    # results is a list of tuples
    results = []
    elip = aws_lib.extract_response(response, "Addresses")
    for e in elip:
        results.append(("E", e["NetworkInterfaceId"], e["PublicIp"]))
    return results


def parse_secg_response(response):
    # results is a list of tuples
    results = []
    secg = aws_lib.extract_response(response, "SecurityGroups")
    for s in secg:
        results.append(("S", s["GroupId"], s["GroupName"], s["Description"]))
        for ip_perm in s["IpPermissions"]:
            if ip_perm["IpProtocol"] != "-1":
                to_port = str(ip_perm["ToPort"])
                for cidr_ip in ip_perm["IpRanges"]:
                    results.append((to_port, cidr_ip["CidrIp"]))
    return results


def parse_vpcs_response(response):
    # results is a list of tuples
    results = []
    vpcs = aws_lib.extract_response(response, "Vpcs")
    for v in vpcs:
        results.append(("C", v["VpcId"], v["CidrBlock"], v["InstanceTenancy"]))
    return results


def get_data_from_region(q, region_name):
    session = boto3.session.Session(region_name=region_name)
    ec2 = session.client("ec2")

    keyp = parse_keyp_response(ec2.describe_key_pairs())
    resv = process_and_parse_resv_response(ec2, ec2.describe_instances())
    vols = parse_vols_response(ec2.describe_volumes())
    neti = parse_neti_response(ec2.describe_network_interfaces())
    elip = parse_elip_response(ec2.describe_addresses())
    secg = parse_secg_response(ec2.describe_security_groups())
    vpcs = parse_vpcs_response(ec2.describe_vpcs())

    q.put((region_name, keyp, resv, vols, neti, elip, secg, vpcs))


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--regions", nargs="*", help="list of regions to query")
    parser.add_argument(
        "-t",
        "--threads",
        action="store_true",
        help="use this argument to run multiple threads",
    )
    args = parser.parse_args()
    ec2 = boto3.client("ec2")
    response = ec2.describe_regions()
    regions = [r for r in response["Regions"]]
    if args.regions:
        # delete the regions that weren't named
        regions = [r for r in regions if r["RegionName"] in args.regions]
    q = queue.Queue()
    thread_list = []
    for region in regions:
        assert 3 == len(region)
        region_name = region["RegionName"]
        assert "ec2.{}.amazonaws.com".format(region_name) == region["Endpoint"]
        if args.threads:
            thread_list.append(
                threading.Thread(target=get_data_from_region, args=(q, region_name))
            )
        else:
            get_data_from_region(q, region_name)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    while not q.empty():
        output_region_data(q.get())
