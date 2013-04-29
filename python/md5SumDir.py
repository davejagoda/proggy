#!/usr/bin/python

import sys, os, hashlib
from os.path import join

CHUNKSIZE = 4096

for path in sys.argv[1:]:
    print(path)
#    for entry in sorted(os.listdir(path)):
    for root, dirs, files in os.walk(sys.argv[1]):
        print 'root', root, 'dirs', dirs, 'files', files
        for entry in files:
            f = open(join(root, entry), 'rb')
            m = hashlib.md5()
            while True:
                chunk = f.read(CHUNKSIZE)
                if chunk:
                    m.update(chunk)
                else:
                    break
            print('MD5 (' + entry + ') = ' +  m.hexdigest())
            f.close
