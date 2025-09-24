#!/usr/bin/env python3

import argparse
import os

TRIPLE_DASH = "---"


def check_for_markdown_front_matter(abs_path):
    with open(abs_path) as f:
        lines = f.readlines()
    if f"{TRIPLE_DASH}\n" != lines[0]:
        print(f"first line is not {TRIPLE_DASH}: {abs_path}")
        return
    for line in lines[1:]:
        if f"{TRIPLE_DASH}\n" == line:
            return
        if line.startswith("title: "):
            continue
        if line.startswith("layout: "):
            continue
        else:
            print(line, end="")


parser = argparse.ArgumentParser()
parser.add_argument("paths", nargs="+", help="the path[s]")
parser.add_argument("-v", "--verbosity", action="count", default=0, help="verbosity")
args = parser.parse_args()
for p in args.paths:
    print(f"Processing: {p}")
    for root, dirs, files in os.walk(p):
        if args.verbosity > 1:
            print(f"root:{root}")
            for d in dirs:
                print(f"dir:{d}")
        for f in files:
            if args.verbosity > 1:
                print(f"file:{f}")
            if f.endswith("md"):
                check_for_markdown_front_matter(os.path.join(root, f))
