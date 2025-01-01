#!/usr/bin/env python2

import argparse
import json
import os
import sys

import simple_salesforce


def query_environment():
    username = os.getenv("SALESFORCE_USERNAME")
    password = os.getenv("SALESFORCE_PASSWORD")
    token = os.getenv("SALESFORCE_SECURITY_TOKEN")
    if username is None:
        print("set the SALESFORCE_USERNAME environment variable")
        sys.exit(1)
    if password is None:
        print("set the SALESFORCE_PASSWORD environment variable")
        sys.exit(1)
    if token is None:
        print("set the SALESFORCE_SECURITY_TOKEN environment variable")
        sys.exit(1)
    return username, password, token


def login(production=True):
    username, password, token = query_environment()
    return simple_salesforce.Salesforce(
        username=username,
        password=password,
        security_token=token,
        client_id="My App",
        sandbox=not production,
    )


def describe_object(sf, sf_object):
    obj = getattr(sf, sf_object).describe()
    assert list == type(obj["fields"])
    return [x["name"] for x in obj["fields"]]


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--production", action="store_true", help="Use production Salesforce instance"
    )
    args = parser.parse_args()
    if args.production:
        print("Using production instance.")
    else:
        print(
            "Using sandbox instance (add --production to access the"
            " production environment)."
        )
    sf = login(args.production)
    field_count = 0
    schema_objects = [x["name"] for x in sf.describe()["sobjects"]]
    for sf_object in schema_objects:
        fields = describe_object(sf, sf_object)
        field_count += len(fields)
        print(sf_object)
        for field in fields:
            print(" {}".format(field))
    print("Total object count:{}".format(len(schema_objects)))
    print("Total field count:{}".format(field_count))
