#!/bin/sh

# https://unix.stackexchange.com/questions/350990/searching-files-containing-non-ascii-characters

LC_ALL=C find . -type f -exec  grep -l '[^[:print:]]' {} \;
