#!/bin/bash

output=$(python -c 'import sys; print(sys.dont_write_bytecode)' | cat)
echo $output

export PYTHONDONTWRITEBYTECODE=1
output=$(python -c 'import sys; print(sys.dont_write_bytecode)' | cat)
echo $output
