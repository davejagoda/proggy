#!/usr/bin/ruby

puts 0.object_id
x = 0
puts x.object_id

puts "0".object_id
x = "0"
puts x.object_id

puts "0".object_id
y = "0"
puts y.object_id

x = :sym
puts x.object_id

y = :sym
puts y.object_id
