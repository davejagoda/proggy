#!/bin/sh

echo 'perl:'

perl -e 'print time; print "\n"'

echo 'python:'

python -c 'import time; print time.time()'

echo 'ruby:'

ruby -e 'puts Time.new().to_f'

echo 'shell:'

date "+%s"
