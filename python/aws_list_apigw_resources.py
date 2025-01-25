#!/usr/bin/env python3

import boto3


def get_resources(client, api_id):
    response = client.get_resources(restApiId=api_id)
    if "items" in response:
        return response.get("items")
    return []


def get_rest_apis(client):
    response = client.get_rest_apis()
    if "items" in response:
        return response.get("items")
    return []


if "__main__" == __name__:
    client = boto3.client("apigateway")
    apis = get_rest_apis(client)
    print("List of API Gateway Instances:")
    for api in apis:
        print(
            f"API ID: {api.get('id')}, Name: {api.get('name')}, Description: {api.get('description', 'No Description')}"
        )
        resources = get_resources(client, api.get("id"))
        for resource in resources:
            resource_id = resource.get("id")
            resource_path = resource.get("path")
            print(f"  Resource ID: {resource_id}, Path: {resource_path}")
