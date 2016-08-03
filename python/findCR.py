#!/usr/bin/python

import sys, codecs, fileinput, string, unicodedata

def process_line(line):
    if '\r' in line:
        print('file:{} line:{}'.format(fileinput.filename(), fileinput.filelineno()))

if '__main__' == __name__:
    current_file = None
    sys.stdin = codecs.getreader('utf-8')(sys.stdin)
    for line in fileinput.input(openhook=fileinput.hook_encoded('utf-8')):
        if fileinput.filename() != current_file:
            current_file = fileinput.filename()
            print('processing:{}'.format(current_file))
        process_line(line)
