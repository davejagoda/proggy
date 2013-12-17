#!/bin/sh

for d in `ls`
do
    cd $d
    ~/Source/Github/Proggy/shell/gitr.sh
    cd ..
    echo
done
