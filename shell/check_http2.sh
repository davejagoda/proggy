#!/bin/bash

if [ 0 == $# ]
then
    echo "Provide at least one URL"
    exit 1
fi

for arg in "$@" ; do
    echo "Checking ${arg}"
    curl --http2 -sI "${arg}" -w '%{http_version}\n'
    echo
done
