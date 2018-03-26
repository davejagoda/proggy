#!/bin/sh

# https://unix.stackexchange.com/questions/268401/why-is-this-find-command-not-returning-filenames-containing-non-ascii-characters

LC_ALL=C find . -name '*[! -~]*'
