#!/usr/bin/ruby

0xa00.upto(0xa7f) {|i| print i, " 0x", i.to_s(16), " ", [i].pack("U*"), "\n"}
