#!/usr/bin/env python3

import argparse
import getpass
import os
import subprocess

DEVNULL = open(os.devnull, "wb")


def validate_password(pswd):
    try:
        subprocess.check_call(
            ["ssh-keygen", "-y", "-f", os.getenv("HOME") + "/.ssh/id_rsa", "-P", pswd],
            stdout=DEVNULL,
            stderr=DEVNULL,
        )
        return True
    except:
        return False


def read_file(file):
    with open(file, "r") as f:
        return [x.strip() for x in f.readlines()]


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="file with words to check")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="show verbose output"
    )
    args = parser.parse_args()
    if args.file:
        for pswd in read_file(args.file):
            if args.verbose:
                print("trying:{}".format(pswd))
            if validate_password(pswd):
                print("valid:{}".format(pswd))
    else:
        pswd = getpass.getpass()
        if validate_password(pswd):
            print("that was it!")
        else:
            print("wrong password")
