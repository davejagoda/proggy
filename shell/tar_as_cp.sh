#!/bin/bash

if [[ $# != 2 ]]
then
    echo "Usage: $0 SRCDIR DSTDIR"
    exit 1
fi

srcdir="$1"
dstdir="$2"

if [[ "${srcdir}" != /* || "${dstdir}" != /* ]]
then
    echo "both paths must be absolute"
    exit 1
fi

cd "${srcdir}" ; tar -cf - . | (cd "${dstdir}" ; tar -xpf -)
