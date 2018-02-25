#!/usr/bin/env python
# -*- coding: utf-8 -*-

# all the non-breaking spaces
#     160       a0   Zs NO-BREAK SPACE
#    8239     202f   Zs NARROW NO-BREAK SPACE
#   65279     feff ﻿ Cf ZERO WIDTH NO-BREAK SPACE

# for formatting:
#      45       2d - Pd HYPHEN-MINUS

print(('{}{}{}'.format(chr(0x2d).encode('utf8'),chr(0x2d).encode('utf8'),chr(0x2d).encode('utf8'))))
print(('{}{}{}'.format(chr(0x2d).encode('utf8'),chr(0xa0).encode('utf8'),chr(0x2d).encode('utf8'))))
print(('{}{}{}'.format(chr(0x2d).encode('utf8'),chr(0x2d).encode('utf8'),chr(0x2d).encode('utf8'))))
print(('{}{}{}'.format(chr(0x2d).encode('utf8'),chr(0x202f).encode('utf8'),chr(0x2d).encode('utf8'))))
print(('{}{}{}'.format(chr(0x2d).encode('utf8'),chr(0x2d).encode('utf8'),chr(0x2d).encode('utf8'))))
print(('{}{}{}'.format(chr(0x2d).encode('utf8'),chr(0xfeff).encode('utf8'),chr(0x2d).encode('utf8'))))
print(('{}{}{}'.format(chr(0x2d).encode('utf8'),chr(0x2d).encode('utf8'),chr(0x2d).encode('utf8'))))
