#!/usr/bin/env python3

# converts SIDs (Nancy Spungen reference)
# very useful resource:
# http://www.selfadsi.org/deep-inside/microsoft-sid-attributes.htm
# another useful resource:
# https://serverfault.com/a/852338
# sample invocation:
# ./nancy.py AQUAAAAAAAUVAAAAPWW1S5rojK4mDAiG5BAAAA==
# expected result:
# S-1-5-21-1270179133-2928470170-2248674342-4324

import argparse, base64, struct


def convertFromSIDString(s):
    return base64.b64decode(s)


def unpackBinarySID(binarySIDString):
    revision, subIDcount, idAuthority, subIDs = struct.unpack(
        ">bb6s20s", binarySIDString
    )
    assert 5 == subIDcount
    first2bytes, last4bytes = struct.unpack(">HI", idAuthority)
    assert 0 == first2bytes
    idAuthority = last4bytes
    listOfIDs = [revision, idAuthority] + list(struct.unpack("<IIIII", subIDs))
    listOfStrings = ["S"] + list(map(str, listOfIDs))
    SID = "-".join(listOfStrings)
    return SID


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("base64encodedSID", help="file to process")
    args = parser.parse_args()
    assert 40 == len(args.base64encodedSID)
    binarySIDString = convertFromSIDString(args.base64encodedSID)
    assert 28 == len(binarySIDString)
    print(unpackBinarySID(binarySIDString))
