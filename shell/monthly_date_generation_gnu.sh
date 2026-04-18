#!/bin/bash

cur_date="2020-01-01"
# Get the first day of the current month
end_date=$(date +%Y-%m-01)

# Loop until the current date exceeds the end date
until [[ "$cur_date" > "$end_date" ]]
do
    echo "$cur_date"
    # Increment the date by exactly one month
    cur_date=$(date -d "$cur_date + 1 month" +%Y-%m-01)
done
