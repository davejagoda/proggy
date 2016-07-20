#!/usr/bin/python

# indentation matters in python

lower =   0 # lower limit of temperature table
upper = 300 # upper limit of temperature table
step =   20 # step size

fahr = lower
while (fahr <= upper):
    celsius = 5 * (fahr - 32) / 9
    print('{}\t{}'.format(fahr, celsius))
    fahr = fahr + step
