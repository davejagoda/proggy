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


# this looks confusing, but
# Once one is inside $(...), quoting starts all over from scratch.
# from https://unix.stackexchange.com/questions/289574/nested-double-quotes-in-highly-voted-one-liner

dqdq="$(basename "tmp/foo bar")"
dqsq="$(basename 'tmp/foo bar')"
if [[ ${dqdq} == ${dqsq} ]]
then
    echo 'SAME: double quote and single quote produce the same results'
else
    echo 'DIFF: double quote and single quote produce different results'
fi
echo "dqdq:${dqdq} dqsq:${dqsq}"
