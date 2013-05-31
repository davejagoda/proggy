#!/usr/bin/python

def bitCheck(i):
    print '{:2d} {:x} {:4b}'.format(i, i, i),
    j = 1
    while True:
        if i & j:
            print 'tail',
        else:
            print 'head',
        j *= 2
        if j > i:
            break
    print

print 'dd x bbbb'
for i in xrange(16):
    bitCheck(i)
