#!/usr/bin/env python3

import sys, subprocess

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " <pcap_file>")
    sys.exit(1)

lines = subprocess.getoutput(
    "/usr/sbin/tcpdump -X -r {}".format(sys.argv[1])
).splitlines()

output_line = ""
for input_line in lines:
    if input_line:
        if input_line[0] == "\t":
            output_line += input_line[51:]
        else:
            print(output_line)
            output_line = input_line

print(output_line)
