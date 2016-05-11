#!/usr/bin/python3

from urllib import request

urls = (['http://davejagoda.nfshost.com/dynamic.php'])

for url in urls:
    print('fetching {} ...'.format(url))
    req = request.Request(url)
    try:
        r = request.urlopen(req)
        print(r.status)
        print(r.read())
    except:
        print('adding a user-agent')
        req.add_header('User-Agent', 'Mozilla/5.0')
        print(r.status)
        print(r.read())
