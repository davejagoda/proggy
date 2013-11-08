#!/usr/bin/python

import sys

# speed of light (meters/second)
C = 299792458.0

# frequency in Hertz (1/second)
f = float(sys.argv[1])

# wavelength (in meters)
print C/f
