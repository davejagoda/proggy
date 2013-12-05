#!/bin/sh

for d in `ls`
do
    cd $d
    pwd
    git branch -a
    git status
    cd ..
    echo
done
