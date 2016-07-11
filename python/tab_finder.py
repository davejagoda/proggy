#!/usr/bin/python

import sys, os

def processDirectory(path):
    for root, dirs, files in os.walk(path):
        for entry in files:
            fullpath = os.path.join(root, entry)
            with open(fullpath, 'rb') as f:
                file_contents = f.read()
                if '\t' in file_contents:
                    print('tab found in {}'.format(fullpath))

def usage():
    print('Usage: ' + sys.argv[0] + ' <directory>')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    processDirectory(sys.argv[1])
