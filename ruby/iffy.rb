#!/usr/bin/ruby

if ARGV.size() != 2
  abort("give me exactly 2 arguments")
end

if ARGV[0] == ARGV[1]
  puts "== eq"
else
  puts "!= ne"
end
