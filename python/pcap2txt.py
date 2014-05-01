#!/usr/bin/python

import sys, subprocess

if len(sys.argv) != 2:
    print 'Usage: ' + sys.argv[0] + ' <pcap_file>'
    sys.exit(1)

bytes = subprocess.check_output(['/usr/sbin/tcpdump', '-X', '-r', sys.argv[1]])

lines = bytes.split(b'\n')

output_line = ''
for input_line in lines:
    if input_line:
        if (input_line[0] == '\t'):
            output_line += input_line[51:]
        else:
            print output_line
            output_line = input_line

print output_line
