#!/usr/bin/python
# make this work on Linux
# 2 relevant files
# /Volumes/<name>/VIDEO_TS/VIDEO_TS.IFO
# /Volumes/<name>/VIDEO_TS/VIDEO_TS.BUP

import argparse, subprocess, re, os

def attach(filename):
    stdout = subprocess.check_output(['hdiutil', 'attach', filename])
# output is tab delimited, thus this would also find the mount name:
# hdiutil attach DVD.iso | cut -f 3
    pattern = '^/dev/disk\d+\s+(/Volumes/.*)$'
    match = re.search(pattern, stdout)
    if args.verbose: print(stdout)
    return(match.group(1))

def detach(volume):
    stdout = subprocess.check_output(['hdiutil', 'detach', volume])
    if args.verbose: print(stdout)
    return

def findFiles(directory, extensions):
    returnList = []
    for extension in extensions:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if re.search(extension, file):
                    if args.verbose: print(os.path.join(root,file))
                    returnList.append(os.path.join(root,file))
    return(returnList)

def readOctets(filename, count):
# read the first count octets of a file, returns ord of the last octet
    if args.verbose: print(filename)
    f = open(filename, 'rb')
    chunk = f.read(count)
    return(ord(chunk[-1]))

def interpretOctet(octet):
    regions = []
    regionpos = 1
    bitwise = 1
    while bitwise < 256:
        if 0 == octet & bitwise:
            regions.append(regionpos)
        bitwise *= 2
        regionpos += 1
    return(regions)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='the file containing the raw DVD image')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    if args.verbose: print('entering main')
    print(args.file)
    volume = attach(args.file)
    files = findFiles(volume, ['IFO','BUP'])
    for file in files:
        result = readOctets(file, 36)
        if 0 != result:
            print(file, interpretOctet(result))
    detach(volume)
    if args.verbose: print('exiting main')
