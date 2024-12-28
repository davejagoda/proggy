#!/usr/bin/env python3

for _, letter in enumerate("rainbow🌈"):
    print("\033[38;5;{}m{}\033[0m".format(_, letter), end="")
print()
