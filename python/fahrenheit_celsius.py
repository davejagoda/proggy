#!/usr/bin/python

# indentation matters in python

lower =   0 # lower limit of temperature table
upper = 300 # upper limit of temperature table
step  =  20 # step size

fahr = lower
while (fahr <= upper):
    celsius = (5.0/9.0) * (fahr-32.0)
    print(('{:3} {:6.1f}'.format(fahr, celsius)))
    fahr = fahr + step
