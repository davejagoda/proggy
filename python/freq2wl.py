#!/usr/bin/env python3

import argparse

# speed of light (meters/second)
C = 299792458.0

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('frequency', type=float, help='frequency in Hertz (1/second)')
    args = parser.parse_args()
    print('wavelength in meters: {}'.format(C/args.frequency))
