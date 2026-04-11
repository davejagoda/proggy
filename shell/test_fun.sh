#!/bin/bash

. $(dirname $0)/test_lib.sh

test-function

test-function () {
    echo "test-function in client"
}

test-function
