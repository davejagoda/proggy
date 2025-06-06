#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# offset controls which day of the week we start with
# offset 0 is Sunday, offset 6 is Saturday
offset = 1  # Monday

import sys

listOfDays = ["日", "月", "火", "水", "木", "金", "土"]
listOfDays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
lenOfWeek = len(listOfDays)
listOfPeople = ["D", "S"]


def usage():
    print("Usage: " + sys.argv[0] + " <list of integers that add up to 14>")
    sys.exit(1)


def checkSumIs14(args):
    values = []
    total = 0
    for i in args:
        total += int(i)
        values.append(int(i))
    if total != 14:
        usage()
    return values


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    values = checkSumIs14(sys.argv[1:])
    s = ""
    for _ in range(lenOfWeek):
        s = s + "{:2}".format(listOfDays[(_ + offset) % lenOfWeek]) + " "
    print(s)
    j = 0
    s = ""
    v = 0  # toggle
    for k in range(2):
        for val in values:
            v += 1
            for i in range(val):
                s = s + listOfPeople[v % 2] + "   "
                j += 1
                if j % lenOfWeek == 0:
                    print(s)
                    s = ""
