#!/usr/bin/env python3

import fileinput


def process_line(line):
    line = line.rstrip()
    print("{} => {}".format(line, line.encode("utf7").decode("ascii")))


if "__main__" == __name__:
    current_file = None
    for line in fileinput.input():
        if fileinput.filename() != current_file:
            current_file = fileinput.filename()
            print("processing:{0}".format(current_file))
        process_line(line)
