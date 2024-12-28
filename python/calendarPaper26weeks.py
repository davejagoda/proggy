#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# if you want to print this out, redirect stdout to a file
# then print it without header and footer, it's an 8.5x11 page

import sys, datetime


def printHeader():
    print(
        """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Calendar Table</title>
<style type="text/css">
  table{
    border: 1px solid black;
    width: 8.5in;
    table-layout: fixed;
  }
  th{
    height: .1in;
  }
  td{
    border: 1px solid black;
    height: .34in;
    vertical-align: top;
    text-align:right;
  }
</style>
</head>
<body>
<table>
<thead>
  <tr>
    <th>日</th>
    <th>月</th>
    <th>火</th>
    <th>水</th>
    <th>木</th>
    <th>金</th>
    <th>土</th>
  </tr>
</thead>
<tbody>
"""
    )


def printFooter():
    print(
        """</tbody>
</table>
</body>
</html>
"""
    )


def getSundayStartDate(d):
    shiftDays = -((d.weekday() + 1) % 7)
    #    print(shiftDays)
    return d + shiftDays * datetime.timedelta(1)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("error: maximum 1 argument")
        sys.exit(1)
    if len(sys.argv) == 2:
        # one argument provided, check if it's a date
        # in the format CCYY-MM-DD
        yy = int(sys.argv[1][0:4])
        mm = int(sys.argv[1][4:6])
        dd = int(sys.argv[1][6:8])
        #        print(yy, mm, dd)
        startDate = datetime.date(yy, mm, dd)
    else:
        startDate = datetime.date.today()

    currDate = getSundayStartDate(startDate)
    printHeader()
    for i in range(26 * 7):
        if i % 7 == 0:
            print("  <tr>")
        print("    <td>", end=" ")
        if i == 0:
            print(currDate.year, currDate.strftime("%b"), currDate.day, end=" ")
        else:
            if currDate.month == 1 and currDate.day == 1:
                print(currDate.year, end=" ")
            if currDate.day == 1:
                print(currDate.strftime("%b"), end=" ")
            print(currDate.day, end=" ")
        print("</td>")
        if i % 7 == 6:
            print("  </tr>")
        currDate = currDate + datetime.timedelta(1)

    printFooter()
