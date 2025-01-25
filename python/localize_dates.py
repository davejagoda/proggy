#!/usr/bin/env python3

import argparse
import datetime
import locale
import os
import re

"""
export LC_ALL=fr_CA.UTF-8
export LC_ALL=ja_JP.UTF-8
export LC_ALL=sv_SE.UTF-8
"""


def process_file(filename, overwrite, verbosity):
    date_pat = r"(\d{4}-\d{2}-\d{2})"
    with open(filename, "r") as f:
        lines = f.readlines()
    if overwrite:
        f = open(filename, "w")
    for line in lines:
        matches = re.findall(date_pat, line)
        if matches:
            if verbosity > 0:
                for match in matches:
                    t = datetime.datetime.fromisoformat(match)
                    replace_match = f"{t.strftime('%B')} {t.day}"
                    print(replace_match)
            # https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-equal
            assert matches.count(matches[0]) == len(matches)
            if overwrite:
                match = matches[0]
                t = datetime.datetime.fromisoformat(match)
                replace_match = f"{t.strftime('%B')} {t.day}"
                f.write(re.sub(match, replace_match, line))
        else:
            if overwrite:
                f.write(line)


if "__main__" == __name__:
    locale.setlocale(locale.LC_ALL, "")
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="+", help="file[s] containing iso8601 dates")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        default=False,
        help="overwrite input files with new dates",
    )
    parser.add_argument(
        "-v", "--verbosity", action="count", default=0, help="verbosity"
    )
    args = parser.parse_args()
    for filename in args.filenames:
        process_file(filename, args.overwrite, args.verbosity)
