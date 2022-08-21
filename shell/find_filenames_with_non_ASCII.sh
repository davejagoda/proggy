#!/bin/sh

# https://unix.stackexchange.com/questions/268401/why-is-this-find-command-not-returning-filenames-containing-non-ascii-characters

LC_ALL=C find . -name '*[! -~]*'

# this would also work:
# LC_ALL=C find . -name '*[^ -~]*'
# You can negate a class by placing a ‘!’ or ‘^’ immediately after the opening bracket.
# https://www.gnu.org/software/findutils/manual/html_mono/find.html#Shell-Pattern-Matching
