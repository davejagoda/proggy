#!/bin/sh

for d in `ls`
do
    cd $d
    pwd
    ~/Source/Github/Proggy/shell/gitr.sh
    cd ..
    echo
done
