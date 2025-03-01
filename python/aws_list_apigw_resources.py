#!/usr/bin/env python3

import argparse
import json
import os

import boto3

LIMIT = 500


# apigateway v1
def get_rest_apis(client, verbosity):
    items = []
    position = None
    while True:
        if position:
            response = client.get_rest_apis(limit=LIMIT, position=position)
        else:
            response = client.get_rest_apis(limit=LIMIT)
        if verbosity > 0:
            print(json.dumps(response, indent=2, sort_keys=True))
        items.extend(response.get("items", []))
        position = response.get("position", None)
        if not position:
            break
    if items:
        return sorted(items, key=lambda x: x["name"])
    return []


def get_resources(client, api_id):
    items = []
    position = None
    while True:
        if position:
            response = client.get_resources(
                restApiId=api_id, embed=["methods"], limit=LIMIT, position=position
            )
        else:
            response = client.get_resources(
                restApiId=api_id, embed=["methods"], limit=LIMIT
            )
        items.extend(response.get("items", []))
        position = response.get("position", None)
        if not position:
            break
    if items:
        return sorted(items, key=lambda x: x["path"])
    return []


def print_last_v1_deployment_date(client, api_id):
    items = []
    position = None
    while True:
        if position:
            response = client.get_deployments(
                restApiId=api_id, limit=LIMIT, position=position
            )
        else:
            response = client.get_deployments(restApiId=api_id, limit=LIMIT)
        items.extend(response.get("items", []))
        position = response.get("position", None)
        if not position:
            break
    if items:
        print(
            sorted(response.get("items"), key=lambda x: x["createdDate"])[-1].get(
                "createdDate"
            )
        )
    else:
        print("Never deployed")


# apigateway v2
def get_apis(client, verbosity):
    items = []
    next_token = None
    while True:
        if next_token:
            response = client.get_apis(NextToken=next_token)
        else:
            response = client.get_apis()
        if verbosity > 0:
            print(json.dumps(response, indent=2, sort_keys=True))
        items.extend(response.get("Items", []))
        next_token = response.get("NextToken", None)
        if not next_token:
            break
    if items:
        return sorted(items, key=lambda x: x["Name"])
    return []


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--details", action="store_true")
    parser.add_argument("-g", "--generic", action="store_true")
    parser.add_argument("-r", "--region", default=os.getenv("AWS_REGION"))
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    args = parser.parse_args()
    # aws apigateway get-rest-apis --output table
    client = boto3.client("apigateway", region_name=args.region)
    apis = get_rest_apis(client, args.verbosity)
    print("List of API Gateway Instances:")
    for api in apis:
        if args.verbosity > 0:
            print(api)
        api_id = api.get("id")
        if args.generic:
            print(f"API Name: {api.get('name')}, ProtocolType: REST")
        else:
            print(
                f"API ID: {api_id}, Name: {api.get('name')}, ProtocolType: REST, Description: {api.get('description', 'No Description')}"
            )
        if args.details:
            resources = get_resources(client, api_id)
            for resource in resources:
                resource_id = resource.get("id")
                resource_path = resource.get("path")
                if args.generic:
                    resource.pop("id")
                    resource.pop("parentId", None)  # root node has no parent
                    print(f"  Path: {resource_path}")
                    print(json.dumps(resource, indent=2, sort_keys=True))
                else:
                    print(f"  Resource ID: {resource_id}, Path: {resource_path}")
                    print(json.dumps(resource, indent=2, sort_keys=True))
        if args.details:
            print_last_v1_deployment_date(client, api_id)
    # aws apigatewayv2 get-apis --output table
    client = boto3.client("apigatewayv2", region_name=args.region)
    apis = get_apis(client, args.verbosity)
    print("List of API GatewayV2 Instances:")
    for api in apis:
        if args.generic:
            print(
                f"API Name: {api.get('Name')}, ProtocolType: {api.get('ProtocolType')}"
            )
        else:
            print(
                f"API ID: {api.get('ApiId')}, Name: {api.get('Name')}, ProtocolType: {api.get('ProtocolType')}, Description: {api.get('Description', 'No Description')}"
            )
