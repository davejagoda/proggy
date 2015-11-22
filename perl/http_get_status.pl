#!/usr/bin/perl

use LWP::UserAgent;

foreach $arg (@ARGV) {
  print $arg."\n";
  my $uri = "http://".$arg;
  my $ua = LWP::UserAgent->new;
  my $response = $ua->head($uri);
  print $response->status_line."\n";
}
