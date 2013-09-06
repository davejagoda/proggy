#!/bin/sh

for d in `ls`
do
    cd $d
    pwd
    git status
    cd ..
done
