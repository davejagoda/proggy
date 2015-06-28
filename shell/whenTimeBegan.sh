#!/bin/bash

for i in `ls /usr/share/zoneinfo/*`
do
    zdump -v $i | head -1 | cut -d " " -f 2-8
done | sort | uniq -c
