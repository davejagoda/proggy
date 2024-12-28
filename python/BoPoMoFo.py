#!/usr/bin/env python3

import unicodedata


def display(i):
    print(i, hex(i), chr(i), unicodedata.name(chr(i)))


print("original range")
for i in range(0x3105, 0x312E):
    display(i)

print("extended range")
for i in range(0x31A0, 0x31BB):
    display(i)
