#!/usr/bin/env python3

import boto3

LIMIT = 500


def get_deployments(client, api_id):
    response = client.get_deployments(restApiId=api_id, limit=LIMIT)
    if "items" in response:
        return response.get("items")
    return []


def get_resources(client, api_id):
    response = client.get_resources(restApiId=api_id, limit=LIMIT)
    if "items" in response:
        return response.get("items")
    return []


def get_rest_apis(client):
    response = client.get_rest_apis(limit=LIMIT)
    if "items" in response:
        return response.get("items")
    return []


if "__main__" == __name__:
    client = boto3.client("apigateway")
    apis = get_rest_apis(client)
    if len(apis) >= LIMIT:
        print("API limit reached")
    print("List of API Gateway Instances:")
    for api in apis:
        print(
            f"API ID: {api.get('id')}, Name: {api.get('name')}, Description: {api.get('description', 'No Description')}"
        )
        resources = get_resources(client, api.get("id"))
        if len(resources) >= LIMIT:
            print("resources limit reached")
        for resource in resources:
            resource_id = resource.get("id")
            resource_path = resource.get("path")
            print(f"  Resource ID: {resource_id}, Path: {resource_path}")
        deployments = get_deployments(client, api.get("id"))
        if len(deployments) >= LIMIT:
            print("deployments limit reached")
        for deployment in deployments:
            deployment_id = deployment.get("id")
            deployment_date = deployment.get("createdDate")
            deployment_description = deployment.get("description")
            if deployment_description is not None:
                deployment_description = deployment_description.replace("\n", "\t")
            print(
                f"  Deployment ID: {deployment_id}, Date: {deployment_date}, {deployment_description}"
            )
