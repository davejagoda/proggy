#!/usr/bin/env python3

import argparse
import difflib
import json
import os


def process_file(filename, check):
    with open(filename, "r") as f:
        original_data = f.read()
        pretty_data = (
            json.dumps(
                json.loads(original_data),
                indent=2,
                separators=(",", ": "),
                sort_keys=True,
            )
            + os.linesep
        )
        if check:
            if pretty_data == original_data:
                print("PRETTY: {}".format(filename))
            else:
                print("NOT_PRETTY: {}".format(filename))
                for line in difflib.unified_diff(
                    pretty_data.splitlines(), original_data.splitlines()
                ):
                    print(line)
        else:
            print("file: {}".format(filename))
            print(pretty_data)
            print()


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="+", help="JSON file[s]")
    parser.add_argument(
        "-c",
        "--check",
        action="store_true",
        default=False,
        help="check if files are pretty",
    )
    args = parser.parse_args()
    for filename in args.filenames:
        process_file(filename, args.check)
