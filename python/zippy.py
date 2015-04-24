#!/usr/bin/python -u

import os, httplib, time

userId = os.getenv('USPSID')
srvr = 'production.shippingapis.com'

for i in xrange(10**5):
    zip = str(i).zfill(5)
    path = '/ShippingAPITest.dll?API=CityStateLookup&XML=<CityStateLookupRequest%20USERID="' +\
           userId +\
           '"><ZipCode%20ID="0"><Zip5>' +\
           zip +\
           '</Zip5></ZipCode></CityStateLookupRequest>'

    print(path)
    conn = httplib.HTTPConnection(srvr)
    conn.request('GET', path)
    resp = conn.getresponse()
    print('status:{} reason:{} data:{}'.format(resp.status, resp.reason, resp.read()))
    conn.close()
#    time.sleep(60) # 70 days!
    time.sleep(10) # 7 days
