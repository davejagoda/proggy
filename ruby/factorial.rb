#!/usr/bin/ruby

def factorial(n)
  retValue = 1
  2.upto(n) do |i|
    retValue *= i
  end
  puts retValue
end

if 1 != ARGV.size()
  puts 'please provide exactly one argument'
else
  factorial(ARGV.pop().to_i)
end
