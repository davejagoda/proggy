#!/usr/bin/python

import datetime
t = datetime.datetime.utcnow().replace(microsecond=0).isoformat()+'Z'
#print(t)

modes = ['a', 'w']
directories = ['/tmp', '/home/dj', '/home/dj/log']

for m in modes:
    for d in directories:
        #print(m, d)
        n = d + '/' + t
        #print(n)
        f=open(n, m)
        f.write(t)
        f.write('\n')
        f.close()

