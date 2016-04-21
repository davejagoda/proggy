#!/usr/bin/python -u

import os, httplib, time

def walk_zips(srvr, userId):
    for i in xrange(10**5):
        zip = str(i).zfill(5)
        path = '/ShippingAPITest.dll?API=CityStateLookup&XML=<CityStateLookupRequest%20USERID="' +\
               userId +\
               '"><ZipCode%20ID="0"><Zip5>' +\
               zip +\
               '</Zip5></ZipCode></CityStateLookupRequest>'
        print(path)
        done = False
        while not done:
            try:
                conn = httplib.HTTPConnection(srvr)
                conn.request('GET', path)
                resp = conn.getresponse()
                print('status:{} reason:{} data:{}'.format(resp.status, resp.reason, resp.read()))
                conn.close()
                done = True
            except Exception as e:
                print('Exception:{}'.format(str(e)))
#        time.sleep(60) # 70 days!
        time.sleep(5) # 3 days
#handle this error more gracefully:
#dj@bothawui:~/Source/GitHub/Proggy/python$ ./zippy.py > zippy.out
#Traceback (most recent call last):
#    File "./zippy.py", line 19, in <module>
#    conn.request('GET', path)
#    File "/usr/lib/python2.7/httplib.py", line 1001, in request
#    self._send_request(method, url, body, headers)
#    File "/usr/lib/python2.7/httplib.py", line 1035, in _send_request
#    self.endheaders(body)
#    File "/usr/lib/python2.7/httplib.py", line 997, in endheaders
#    self._send_output(message_body)
#    File "/usr/lib/python2.7/httplib.py", line 850, in _send_output
#    self.send(msg)
#    File "/usr/lib/python2.7/httplib.py", line 812, in send
#    self.connect()
#    File "/usr/lib/python2.7/httplib.py", line 793, in connect
#    self.timeout, self.source_address)
#    File "/usr/lib/python2.7/socket.py", line 571, in create_connection
#    raise err
#socket.error: [Errno 110] Connection timed out
#

if '__main__' == __name__:
    srvr = 'production.shippingapis.com'
    userId = os.getenv('USPSID')
    if (userId):
        walk_zips(srvr, userId)
    else:
        print('set USPSID environment variable')
