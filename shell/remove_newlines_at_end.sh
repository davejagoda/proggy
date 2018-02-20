#!/bin/bash

# https://unix.stackexchange.com/questions/81685/how-to-remove-multiple-newlines-at-eof

usage ()
{
    echo "Please an argument to pass to unix 'find . -name'"
    echo "You may need to quote it"
    echo "E.g. $0 '*.py'"
    exit 1
}

if ! [[ 1 -eq $# ]]
then
    usage
fi

case $(uname) in
    Darwin)
        inline="-i''"
        ;;
    Linux)
        inline="-i"
        ;;
    *)
        echo "Unknown OS"
        exit 1
        ;;
esac

echo "${1}"
echo "${inline}"
$(find . -type f -name "${1}" -exec sed "${inline}" -e :a -e '/^\n*$/{$d;N;};/\n$/ba' {} \;)
