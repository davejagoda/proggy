#!/usr/bin/python

import datetime
t = datetime.datetime.utcnow().replace(microsecond=0).isoformat()+'Z'
#print(t)

modes = ['w', 'a']
directories = ['/tmp', '/home/dj']

for m in modes:
    for d in directories:
        #print(m, d)
        n = d + '/' + t
        #print(n)
        f=open(n, m)
        f.write(t)
        f.write('\n')
        f.close()

