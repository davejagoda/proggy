#!/usr/bin/env python3

# print out:
# 1) the first line of the file
# 2) the first line after 2 blank lines

import sys

if __name__ == "__main__":
    f = open(sys.argv[1])

    new_para = True
    out_line = ""
    for line in f.readlines():
        if line == "\n":
            new_para = True
        else:
            if new_para:
                if len(out_line) > 0:
                    print(out_line)
                new_para = False
                out_line = line.rstrip("\n") + ":"
            else:
                out_line += line.rstrip("\n")

    f.close()
    if len(out_line) > 0:
        print(out_line)
