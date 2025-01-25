#!/usr/bin/env python3

import boto3


def list_api_gateways():
    client = boto3.client("apigateway")

    response = client.get_rest_apis()

    # Check if there are any APIs
    if "items" in response:
        print("List of API Gateway Instances:")
        for api in response["items"]:
            print(
                f"API ID: {api['id']}, Name: {api['name']}, Description: {api.get('description', 'No Description')}"
            )
            resources_response = client.get_resources(restApiId=api["id"])
            if "items" in resources_response:
                for resource in resources_response["items"]:
                    resource_id = resource["id"]
                    resource_path = resource["path"]
                    print(f"  Resource ID: {resource_id}, Path: {resource_path}")
            else:
                print(f"No resources found for API {api['name']}.")

    else:
        print("No API Gateway instances found.")



if "__main__" == __name__:
    list_api_gateways()
