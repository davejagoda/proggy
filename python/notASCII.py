#!/usr/bin/python

import sys, codecs, fileinput, string, unicodedata

def emit_output(filename, linenumber, character, charactername):
    print(('file:{0} line:{1} -> {2}:{3}'.format(filename, linenumber, character, charactername)))

def process_line(line):
    for datum in line:
        if datum not in string.printable:
            try:
                charactername = unicodedata.name(datum)
            except:
                charactername = 'no such unicode name exists'
            emit_output(fileinput.filename(), fileinput.filelineno(), datum.encode('utf-8'), charactername)

if '__main__' == __name__:
    current_file = None
    sys.stdin = codecs.getreader('utf-8')(sys.stdin)
    for line in fileinput.input(openhook=fileinput.hook_encoded('utf-8')):
        if fileinput.filename() != current_file:
            current_file = fileinput.filename()
            print(('processing:{0}'.format(current_file)))
        process_line(line)
