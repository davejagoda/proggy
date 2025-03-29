#!/usr/bin/env python3
import argparse
import collections
import datetime
import json
import os
import sys

import openpyxl

parser = argparse.ArgumentParser()
parser.add_argument("command", help="sed like s command such as %this%that%")
parser.add_argument("infile", help="the source spreadsheet")
parser.add_argument("outfile", help="the destination spreadsheet")
parser.add_argument("-v", "--verbose", action="count", default=0)
args = parser.parse_args()

wb = openpyxl.load_workbook(filename=args.infile)
print(f"processing workbook: {args.infile}")

search_str = None
replace_str = None
if args.command[0] == args.command[-1]:
    fields = args.command.split(args.command[0])
    if args.verbose > 0:
        print(fields)
    if 4 == len(fields):
        search_str = fields[1]
        replace_str = fields[2]
if search_str == replace_str:
    print(f"malformed command string: {args.command}")
    sys.exit(1)

modified = False
for ws in wb.worksheets:
    print(f"processing worksheet: {ws.title}")
    for row in ws.rows:
        for cell in row:
            if args.verbose:
                print(cell.value)
            if cell.value and search_str in cell.value:
                modified = True
                cell.value = cell.value.replace(search_str, replace_str)
if modified:
    if os.path.exists(args.outfile):
        print(f"file {args.outfile} already exists, refusing to overwrite")
        sys.exit(1)
    wb.save(args.outfile)
    print(f"wrote workbook: {args.outfile}")
