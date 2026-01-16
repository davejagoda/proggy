#!/usr/bin/perl

# https://stackoverflow.com/questions/5917576/sort-a-text-file-by-line-length-including-spaces/40786477#40786477

print sort { length($a) <=> length($b) } <>
