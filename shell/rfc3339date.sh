#!/bin/sh
echo 'date --rfc-3339=seconds'
date --rfc-3339=seconds
echo 'date +"%Y-%m-%dT%H:%M:%S%:%z"'
date +'%Y-%m-%dT%H:%M:%S%:z'
