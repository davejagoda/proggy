#!/usr/bin/python

import sys, os

def processDirectory(path, size):
#from os.path import join
    for root, dirs, files in os.walk(path):
#        print 'root', root, 'dirs', dirs, 'files', files
        for entry in files:
#            f = open(join(root, entry), 'rb')
            fullpath = os.path.join(root, entry)
#            print(fullpath + ':' + str(os.path.getsize(fullpath)))
            if os.path.getsize(fullpath) <= size:
                f = open(os.path.join(root, entry), 'rb')
                print 'reading', entry
                print f.read()
                f.close
                print 'closing'
                input_prompt = 'Press Y to delete file: ' + fullpath + ', anything else to keep it: '
                response = raw_input(input_prompt)
                if response == 'Y':
                    os.unlink(fullpath)

def usage():
    print('Usage: ' + sys.argv[0] + ' <directory> [<max file size>]')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        usage()
    if len(sys.argv) == 3:
        try:
            maxSize = int(sys.argv[2])
        except:
            usage()
    else:
        maxSize = 0
    processDirectory(sys.argv[1], maxSize)
