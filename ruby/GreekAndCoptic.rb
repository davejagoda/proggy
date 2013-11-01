#!/usr/bin/ruby

0x370.upto(0x3ff) {|i| print i, " 0x", i.to_s(16), " ", [i].pack("U*"), "\n"}
