#!/usr/bin/ruby

i = 0x1f000
while i < 0x1ffff
  print [i].pack("U*")
  i += 1
end
