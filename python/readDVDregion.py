#!/usr/bin/env python3

# 2 relevant files
# VIDEO_TS/VIDEO_TS.IFO
# VIDEO_TS/VIDEO_TS.BUP

import argparse
import os
import platform
import re
import subprocess


def attach_osx(filename):
    stdout = subprocess.getoutput("hdiutil attach {}".format(filename))
    # output is tab delimited, thus this would also find the mount name:
    # hdiutil attach DVD.iso | cut -f 3
    pattern = "^/dev/disk\d+\s+(/Volumes/.*)$"
    match = re.search(pattern, stdout)
    if args.verbose:
        print(stdout)
    return match.group(1)


def attach_linux(filename):
    tmpdir = subprocess.getoutput("mktemp -d")
    stdout = subprocess.getoutput("archivemount {} {}".format(filename, tmpdir))
    return tmpdir


def detach_osx(volume):
    stdout = subprocess.getoutput("hdiutil detach {}".format(volume))
    if args.verbose:
        print(stdout)
    return


def detach_linux(volume):
    stdout = subprocess.getoutput("fusermount -u {}".format(volume))
    if args.verbose:
        print(stdout)
    return


def findFiles(directory, extensions):
    returnList = []
    for extension in extensions:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if re.search(extension, file):
                    if args.verbose:
                        print(os.path.join(root, file))
                    returnList.append(os.path.join(root, file))
    return returnList


def readOctets(filename, count):
    # read the first count octets of a file, return the last octet
    if args.verbose:
        print(filename)
    f = open(filename, "rb")
    chunk = f.read(count)
    return chunk[-1]


def interpretOctet(octet):
    regions = []
    regionpos = 1
    bitwise = 1
    while bitwise < 256:
        if 0 == octet & bitwise:
            regions.append(regionpos)
        bitwise *= 2
        regionpos += 1
    return regions


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="the file containing the raw DVD image")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    if "Darwin" == platform.system():
        volume = attach_osx(args.file)
    else:
        volume = attach_linux(args.file)
    files = findFiles(volume, ["IFO", "BUP"])
    for file in files:
        result = readOctets(file, 36)
        if 0 != result:
            print(file, interpretOctet(result))
    if "Darwin" == platform.system():
        detach_osx(volume)
    else:
        detach_linux(volume)
