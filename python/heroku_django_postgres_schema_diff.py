#!/usr/bin/env python2

# similar to this:
# diff -U 0 *schema

import argparse
import difflib
import os
import re
import subprocess
import sys

import urlparse


def transform_owner(s, owner_name, verbose):
    # validate the file and set owner if not provided
    for line in s:
        m = re.search(r"Owner: (\S+)$", line)
        if m:
            if None == owner_name:
                owner_name = m.group(1)
                if verbose > 0:
                    print("transform_owner found owner:{}".format(owner_name))
            assert owner_name == m.group(1)
        m = re.search(r"OWNER TO (\S+);$", line)
        if m:
            if None == owner_name:
                owner_name = m.group(1)
            assert owner_name == m.group(1)
    # fix up the file
    new_s = []
    for line in s:
        line = re.sub("Owner: {}".format(owner_name), "Owner: schema_owner", line)
        line = re.sub("OWNER TO {};".format(owner_name), "OWNER TO schema_owner;", line)
        new_s.append(line)
    return new_s


def transform_fk_constraints(s):
    new_s = []
    for line in s:
        line = re.sub(r"_id_[0-9a-f]{8,16}_fk", "_id_#_fk", line)
        new_s.append(line)
    return new_s


def transform_uk_constraints(s):
    new_s = []
    for line in s:
        line = re.sub(r"_[0-9a-f]{8,16}_uniq", "_#_uniq", line)
        new_s.append(line)
    return new_s


def get_dburl_from_app_name(app_name, verbose):
    if verbose > 0:
        print("getting dburl from app name")
    return subprocess.check_output(
        ["heroku", "config:get", "DATABASE_URL", "-a", app_name]
    ).rstrip()


def get_dburl_from_remote_name(remote_name, verbose):
    if verbose > 0:
        print("getting dburl from remote name")
    return subprocess.check_output(
        ["heroku", "config:get", "DATABASE_URL", "-r", remote_name]
    ).rstrip()


def parse_dburl(dburl, verbose):
    if verbose > 0:
        print("this is a dburl:{}".format(dburl))
    # should handle no username, no password, and no port in dburl
    o = urlparse.urlparse(dburl)
    dbname = o.path[1:] or "postgres"
    dbhost = o.hostname or "localhost"
    dbport = str(o.port) or "5432"
    dbuser = o.username or "postgres"
    dbpass = o.password or "postgres"
    if verbose > 0:
        print(dbname, dbhost, dbport, dbuser, dbpass)
    return (dbname, dbhost, dbport, dbuser, dbpass)


def get_data_from_dburl(dburl, verbose):
    (dbname, dbhost, dbport, dbuser, dbpass) = parse_dburl(dburl, verbose)
    if verbose > 0:
        print("getting data from dburl")
    env = os.environ
    env["PGPASSWORD"] = dbpass
    return subprocess.check_output(
        ["pg_dump", "-s", "-d", dbname, "-h", dbhost, "-p", dbport, "-U", dbuser],
        env=env,
    ).splitlines()


def get_data_from_file(filename):
    with open(filename, "r") as f:
        return f.readlines()


def write_file(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    # s is for source
    parser.add_argument("s1", help="source 1")
    parser.add_argument("s2", help="source 2")
    parser.add_argument(
        "--no_owner_xform", action="store_true", help="do not xform owner"
    )
    parser.add_argument(
        "--no_fk_xform",
        action="store_true",
        help="do not xform foreign key constraints",
    )
    parser.add_argument(
        "--no_uk_xform", action="store_true", help="do not xform unique key constraints"
    )
    parser.add_argument("-w", "--write", action="store_true", help="write xformed data")
    parser.add_argument("-v", "--verbose", action="count", help="verbose output")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-a",
        "--app",
        action="store_true",
        help="use heroku app config to get DBURL for schema",
    )
    group.add_argument(
        "-r",
        "--remote",
        action="store_true",
        help="use heroku remote config to get DBURL for schema",
    )
    group.add_argument(
        "-d", "--dburl", action="store_true", help="use DBURL to get schema"
    )
    group.add_argument(
        "-f", "--file", action="store_true", help="sources contain schema dump"
    )
    args = parser.parse_args()
    u1 = None
    u2 = None
    if args.app:
        u1 = get_dburl_from_app_name(args.s1, args.verbose)
        u2 = get_dburl_from_app_name(args.s2, args.verbose)
    if args.remote:
        u1 = get_dburl_from_remote_name(args.s1, args.verbose)
        u2 = get_dburl_from_remote_name(args.s2, args.verbose)
    if args.dburl:
        u1 = args.s1
        u2 = args.s2
    if args.file:
        owner_name = None
        d1 = get_data_from_file(args.s1)
        d2 = get_data_from_file(args.s2)
    else:
        d1 = get_data_from_dburl(u1, args.verbose)
        d2 = get_data_from_dburl(u2, args.verbose)
    if not args.no_owner_xform:
        (_, _, _, o1, _) = parse_dburl(u1, args.verbose)
        d1 = transform_owner(d1, o1, args.verbose)
        (_, _, _, o2, _) = parse_dburl(u2, args.verbose)
        d2 = transform_owner(d2, o2, args.verbose)
    if not args.no_fk_xform:
        d1 = transform_fk_constraints(d1)
        d2 = transform_fk_constraints(d2)
    if not args.no_uk_xform:
        d1 = transform_uk_constraints(d1)
        d2 = transform_uk_constraints(d2)
    if args.write:
        f1 = "f1.out"
        f2 = "f2.out"
        if os.path.exists(f1) or os.path.exists(f2):
            print("refusing to overwrite {} or {} file".format(f1, f2))
        else:
            write_file(f1, d1)
            write_file(f2, d2)
    else:
        for line in difflib.unified_diff(d1, d2, n=0):
            sys.stdout.write(line)
