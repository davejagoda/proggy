#!/usr/bin/ruby

include Math

n = 1

while ((n - cos(n)).abs > 0.000000000000001)
    print n, " ", n - cos(n), "\n"
    n = cos(n)
end
