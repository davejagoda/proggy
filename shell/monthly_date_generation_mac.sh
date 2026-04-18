#!/bin/bash

# current year / month for the stop condition
end_year=$(date +%Y)
end_month=$(date +%m)

# start year / month
year=2020
month=1

# loop until reaching the current year / month
while [ "$year" -lt "$end_year" ] || [ "$month" -le "$end_month" ]
do
    # %02g ensures the month always has two decimal (not octal) digits
    printf "%g-%02g-01\n" "$year" "$month"
    month=$((month + 1))
    if [ "$month" -gt 12 ]; then
        month=1
        year=$((year + 1))
    fi
done
