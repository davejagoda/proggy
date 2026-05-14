#!/usr/bin/env python3

import argparse
import datetime
import re

parser = argparse.ArgumentParser()
parser.add_argument("iso8601date", help="Date in YYYY-MM-DD format")
args = parser.parse_args()

iso8601pat = r"^\d{4}-\d{2}-\d{2}$"

m = re.match(iso8601pat, args.iso8601date)

if m:
    t = datetime.datetime.strptime(args.iso8601date, "%Y-%m-%d")
    w = t + datetime.timedelta(days=1)
    print(w.date())
else:
    print(f"Error: '{args.iso8601date}' is not in YYYY-MM-DD format")
