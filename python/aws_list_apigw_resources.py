#!/usr/bin/env python3

import argparse
import json

import boto3

LIMIT = 500


def get_rest_apis(client):
    response = client.get_rest_apis(limit=LIMIT)
    if "items" in response:
        return sorted(response.get("items"), key=lambda x: x["name"])
    return []


def get_resources(client, api_id):
    response = client.get_resources(restApiId=api_id, limit=LIMIT)
    if "items" in response:
        return sorted(response.get("items"), key=lambda x: x["path"])
    return []


def get_deployments(client, api_id):
    response = client.get_deployments(restApiId=api_id, limit=LIMIT)
    if "items" in response:
        return sorted(response.get("items"), key=lambda x: x["createdDate"])
    return []


def get_last_deployment(client, api_id, deployment_id):
    response = client.get_deployment(
        restApiId=api_id, deploymentId=deployment_id, embed=["apisummary"]
    )
    if "apiSummary" in response:
        return response.get("apiSummary")
    return []


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()
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
        if args.verbose > 0:
            for deployment in deployments:
                deployment_id = deployment.get("id")
                deployment_date = deployment.get("createdDate")
                deployment_description = deployment.get("description")
                if deployment_description is not None:
                    deployment_description = deployment_description.replace("\n", "\t")
                print(
                    f"  Deployment ID: {deployment_id}, Date: {deployment_date}, {deployment_description}"
                )
        else:
            if [] == deployments:
                print(f"No deployments for API ID: {api.get('id')}")
            else:
                deployment_id = deployments[-1].get("id")
                deployment_date = deployments[-1].get("createdDate")
                print(f"Deployment ID: {deployment_id}, Date: {deployment_date}")
                print(
                    json.dumps(
                        get_last_deployment(client, api.get("id"), deployment_id),
                        indent=2,
                        sort_keys=True,
                    )
                )
