#!/bin/bash

vars=(
    hoge
    fuga
    piyo
)
length=${#vars[@]}
echo "length: ${length}"
echo "first: ${vars[0]}"
echo "last: ${vars[${length}-1]}"
echo "here is the entire array:"
for var in "${vars[@]}"
do
    echo "${var}"
done
echo "here is the space-separated list"
echo "${vars[@]}"
