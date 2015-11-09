#!/bin/bash

output=`python -c 'import sys; print(sys.stdout.encoding)' | cat`
echo $output

export PYTHONIOENCODING=UTF-8
output=`python -c 'import sys; print(sys.stdout.encoding)' | cat`
echo $output
