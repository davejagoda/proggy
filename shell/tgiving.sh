#!/bin/bash

i=2000

while [[ ${i} -lt 2030 ]]
do
    cal 11 ${i} | grep -C 10 "             1  2  3"
    i=$((i+1))
done
