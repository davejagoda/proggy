#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# all the non-breaking spaces
#     160       a0   Zs NO-BREAK SPACE
#    8239     202f   Zs NARROW NO-BREAK SPACE
#   65279     feff ﻿ Cf ZERO WIDTH NO-BREAK SPACE

# for formatting:
#      45       2d - Pd HYPHEN-MINUS

print('{}{}{}'.format(chr(0x2d),chr(0x2d),chr(0x2d)))
print('{}{}{}'.format(chr(0x2d),chr(0xa0),chr(0x2d)))
print('{}{}{}'.format(chr(0x2d),chr(0x2d),chr(0x2d)))
print('{}{}{}'.format(chr(0x2d),chr(0x202f),chr(0x2d)))
print('{}{}{}'.format(chr(0x2d),chr(0x2d),chr(0x2d)))
print('{}{}{}'.format(chr(0x2d),chr(0xfeff),chr(0x2d)))
print('{}{}{}'.format(chr(0x2d),chr(0x2d),chr(0x2d)))
