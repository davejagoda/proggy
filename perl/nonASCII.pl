#!/usr/bin/perl

foreach $file (@ARGV) {
    open(my $fh, "<", $file)
	or die "cannot open < $file: $!";
    while (<$fh>) {
	if (m/[[:^ascii:]]/) {
	    print;
	}
    }
}
