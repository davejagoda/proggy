#!/usr/bin/ruby

def slow_way(lower,upper)
# check every number if it is divisible by 9
  count = 0
  temp = 0
  t0 = Time.new().to_i
  lower.upto(upper) do |i|
    if (i % 9 == 0)
      count += 1
      if (temp == 0)
        print "a: ", i, "\n"
      end
      temp = i
    end
  end
  print "z: ", temp, "\n"
  t1 = Time.new().to_i
  print "found: ", count, " numbers in ", t1-t0, " seconds\n\n"
end

def fast_way(lower,upper)
# find the first number and keep adding 9
  count = 0
  temp = 0
  incr = 1
  i = lower
  t0 = Time.new().to_i
  while(i <= upper) do
    if (incr == 9)
      count += 1
      temp = i
    elsif (i % 9 == 0)
      count += 1
      print "a: ", i, "\n"
      incr = 9
    end
    i += incr
  end
  print "z: ", temp, "\n"
  t1 = Time.new().to_i
  print "found: ", count, " numbers in ", t1-t0, " seconds\n\n"
end

def best_way(lower,upper)
# find the first, find how many, find the last
  t0 = Time.new().to_i
  i = ( lower / 9 ) * 9
  n = ( upper - lower + 1 ) / 9
  if ( i != lower )
    i += 9
  end
  print "a: ", i , "\n"
  print "z: ", i + ( ( n - 1) * 9 ), "\n"
  t1 = Time.new().to_i
  print "found: ", n, " numbers in ", t1-t0, " seconds\n\n"
end

if __FILE__ == $0
  ####### 123456789 # smallest and largest 9 digit numbers:
  lower = 100000000
  upper = 999999999
  puts "~370 seconds vs. ~66 seconds vs. 0 seconds"
  puts "#a: 100000008 #z: 999999999 #found: 100000000 numbers"
  puts
  best_way(lower,upper)
  fast_way(lower,upper)
  slow_way(lower,upper)
end
