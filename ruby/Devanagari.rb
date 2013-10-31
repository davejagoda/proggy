#!/usr/bin/ruby

0x900.upto(0x97f) {|i| print i, " 0x", i.to_s(16), " ", [i].pack("U*"), "\n"}
