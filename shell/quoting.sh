#!/bin/bash

# this will produce two lines of output
# ./quoting.sh foo bar

# these next two will each produce one line of output
# ./quoting.sh 'foo bar'
# ./quoting.sh "foo bar"

if [[ 0 == $# ]]
then
    echo 'no arguments provided'
else
    # need "$@" to preserve spaces in arguments
    for arg in "$@"
    do
        echo ${arg}
    done
fi
