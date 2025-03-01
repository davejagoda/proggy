#!/usr/bin/env python3

import argparse
import collections
import datetime
import json

parser = argparse.ArgumentParser()
parser.add_argument("log_files", nargs="+", help="the log file[s]")
parser.add_argument("-v", "--verbosity", action="count", default=0, help="verbosity")
args = parser.parse_args()
for log_file in args.log_files:
    print(f"Processing {log_file}")
    oldest = None
    newest = None
    apigws = collections.Counter()
    clf = collections.Counter()
    with open(log_file) as f:
        for line in f.readlines():
            fields = line.split(" ")
            iso8601 = fields[0]
            if args.verbosity > 1:
                print(iso8601)
            dt = datetime.datetime.fromisoformat(iso8601)
            if oldest is None or oldest > dt:
                oldest = dt
            if newest is None or newest < dt:
                newest = dt
            apigw_instance = fields[1]
            if args.verbosity > 0:
                print(apigw_instance)
            apigws[apigw_instance] += 1
            if "INFO:" == fields[2]:
                remainder = " ".join(fields[2:])
                if args.verbosity > 1:
                    print(remainder)
                lhs, rhs = remainder.split("-")
                rhs = rhs.strip()
                if args.verbosity > 1:
                    print(rhs)
                clf[rhs] += 1
        print(f"oldest:{oldest} newest:{newest} elapsed:{newest - oldest}")
        print(json.dumps(apigws, indent=2, sort_keys=True))
        print(json.dumps(clf, indent=2, sort_keys=True))
