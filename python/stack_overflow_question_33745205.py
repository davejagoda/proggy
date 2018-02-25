#!/usr/bin/env python3

from urllib import request

urls = (
    'http://math.stackexchange.com/election/5?tab=primary',
    'http://serverfault.com/election/5?tab=primary',
    'http://stackoverflow.com/election/7?tab=primary',
)

for url in urls:
    print(('fetching {} ...'.format(url)))
    try:
        request.urlopen(url).read()
    except:
        print('got an exception, changing user-agent to urllib3 default')
        req = request.Request(url)
        req.add_header('User-Agent', 'Python-urllib/3.4')
        try:
            request.urlopen(req)
        except:
            print('got another exception, changing user-agent to something else')
            req.add_header('User-Agent', 'not-Python-urllib/3.4')
            request.urlopen(req)
