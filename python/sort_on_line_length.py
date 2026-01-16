#!/usr/bin/env python3

# https://stackoverflow.com/questions/5917576/sort-a-text-file-by-line-length-including-spaces/71484419#71484419

import fileinput
import sys

# sys.stdout.writelines(sorted(fileinput.input(), key=len))
print("".join(sorted(fileinput.input(), key=len)), end="")
