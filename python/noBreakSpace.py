#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# all the non-breaking spaces
#     160       a0   Zs NO-BREAK SPACE
#    8239     202f   Zs NARROW NO-BREAK SPACE
#   65279     feff ﻿ Cf ZERO WIDTH NO-BREAK SPACE

# for formatting:
#      45       2d - Pd HYPHEN-MINUS

print("{}{}{}".format(chr(0x2D), chr(0x2D), chr(0x2D)))
print("{}{}{}".format(chr(0x2D), chr(0xA0), chr(0x2D)))
print("{}{}{}".format(chr(0x2D), chr(0x2D), chr(0x2D)))
print("{}{}{}".format(chr(0x2D), chr(0x202F), chr(0x2D)))
print("{}{}{}".format(chr(0x2D), chr(0x2D), chr(0x2D)))
print("{}{}{}".format(chr(0x2D), chr(0xFEFF), chr(0x2D)))
print("{}{}{}".format(chr(0x2D), chr(0x2D), chr(0x2D)))
