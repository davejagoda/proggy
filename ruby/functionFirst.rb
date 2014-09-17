#!/usr/bin/ruby

# Ruby requires the function to be defined first

def fun()
    puts "inside function fun"
end

if __FILE__ == $0
    fun()
    puts "hello function first"
end
