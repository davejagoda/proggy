#!/bin/bash

usage () {
    echo "$0 dosfile unixfile"
    echo "dosfile is read"
    echo "unixfile is truncated then written"
    echo "dosfile and unixfile must be different files"
}

if [ 2 != $# ]; then
    usage
    exit 1
fi

DOSFILE=$1
UNIXFILE=$2

if [ $DOSFILE = $UNIXFILE ]; then
    usage
    exit 1
fi

tr -d '\15' < $DOSFILE > $UNIXFILE
