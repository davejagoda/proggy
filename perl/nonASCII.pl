#!/usr/bin/perl


while (<>) {
    if (m/[[:^ascii:]]/) {
        print;
    }
}
