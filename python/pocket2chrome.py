#!/usr/bin/env python

import argparse
import os
import sys

preamble = '''<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
    <DT><H3>Pocket Bookmarks</H3>
    <DL><p>
'''

amble = '        <DT><A HREF="{}">{}</A>\n'

postamble = '''    </DL><p>
</DL><p>
'''

parser = argparse.ArgumentParser()
parser.add_argument('pocket', help='input text file containing exported Pocket URLs')
parser.add_argument('chrome', help='output HTML file suitable for importing to Chrome')
parser.add_argument('-f', '--force', action='store_true', help='allow overwriting Chome bookmarks file')
parser.add_argument('-v', '--verbose', action='count', help='show verbose output')
args = parser.parse_args()

if not os.path.exists(args.pocket):
    print('pocket export file not found')
    sys.exit(1)
if os.path.exists(args.chrome) and not args.force:
    print args.force
    print('bookmarks exists, refusing to overwrite')
    sys.exit(1)

with open(args.pocket, 'r') as f_in:
    with open(args.chrome, 'w') as f_out:
        f_out.write(preamble)
        for line in f_in.xreadlines():
            if 2 < args.verbose:
                print(line.rstrip())
            parts = line.split(' | ')
            if 1 < args.verbose and 2 != len(parts):
                print('found multiple delimiters in this line:{}'.format(line.rstrip()))
            f_out.write(amble.format(parts[0], ' | '.join(parts[1:]).rstrip()))
        f_out.write(postamble)
