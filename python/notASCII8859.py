#!/usr/bin/env python3

import codecs
import fileinput
import string
import sys
import unicodedata


def emit_output(filename, linenumber, character, charactername):
    print(
        "file:{0} line:{1} -> {2}:{3}".format(
            filename, linenumber, character, charactername
        )
    )


def process_line(line):
    for datum in line:
        if datum not in string.printable:
            try:
                charactername = unicodedata.name(datum)
            except:
                charactername = "no such unicode name exists"
            emit_output(
                fileinput.filename(), fileinput.filelineno(), datum, charactername
            )


if "__main__" == __name__:
    current_file = None
    sys.stdin = codecs.getreader("iso8859-1")(sys.stdin)
    # https://docs.python.org/3/howto/unicode.html#converting-to-bytes
    for line in fileinput.input(
        openhook=fileinput.hook_encoded("iso8859-1", "replace")
    ):
        if fileinput.filename() != current_file:
            current_file = fileinput.filename()
            print("processing:{0}".format(current_file))
        process_line(line)
