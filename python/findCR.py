#!/usr/bin/env python3

import codecs
import fileinput
import string
import sys

def process_line(line):
    if '\r'.encode() in line:
        print('file:{0} line:{1}'.format(fileinput.filename(),
                                         fileinput.filelineno()))

if '__main__' == __name__:
    current_file = None
    sys.stdin = codecs.getreader('utf-8')(sys.stdin)
    for line in fileinput.input(mode='rb'):
        if fileinput.filename() != current_file:
            current_file = fileinput.filename()
            print('processing:{0}'.format(current_file))
        process_line(line)
