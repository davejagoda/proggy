#!/usr/bin/python

import pprint

lc = [x for x in xrange(10)]

print(lc)

dc = {x: chr(96 + x) for x in xrange(1, 27) }

pprint.pprint(dc, width=1)
