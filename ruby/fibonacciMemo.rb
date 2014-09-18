#!/usr/bin/ruby

# https://defuse.ca/blog/my-favorite-rubyisms.html

fibonacci = Hash.new do |h,k|
  h[k] = k >= 2 ? h[k-1] + h[k-2] : 1
end

0.upto(100) { |i| puts fibonacci[i] }
