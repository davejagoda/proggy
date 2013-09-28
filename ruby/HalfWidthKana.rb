#!/usr/bin/ruby

#for i in (0xff65..0xff9f)
(0xff65..0xff9f).each do |i|
    print i.to_s(16), ":", [i.to_s(16).to_i(16)].pack("U*"), "\n"
end
