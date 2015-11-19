#!/usr/bin/ruby

require 'net/http'

for arg in ARGV
  puts arg
  uri = URI('http://' + arg)
  res = Net::HTTP.get_response(uri)
  puts res.code
end
