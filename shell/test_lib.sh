#!/bin/bash

# this is a library of functions
# to include them add this to the calling script:
# . $(dirname $0)/test_lib.sh
# list functions in alphabetic order

test-function () {
    echo "test-function in library"
}
