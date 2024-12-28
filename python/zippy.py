#!/usr/bin/env python3

import os, http.client, time, xml.etree.ElementTree


def walk_zips(srvr, userId):
    #    for i in range(9999,10010):
    for i in range(10**5):
        zip = str(i).zfill(5)
        path = (
            "/ShippingAPITest.dll?API="
            + "CityStateLookup&XML="
            + '<CityStateLookupRequest%20USERID="'
            + userId
            + '"><ZipCode%20ID="0"><Zip5>'
            + zip
            + "</Zip5></ZipCode></CityStateLookupRequest>"
        )
        done = False
        while not done:
            try:
                conn = http.client.HTTPConnection(srvr)
                conn.request("GET", path)
                resp = conn.getresponse()
                if 200 == resp.status:
                    root = xml.etree.ElementTree.fromstring(resp.read())
                    #                    for r in root[0]:
                    #                        print(r.tag, r.text, flush=True)
                    if "Zip5" != root[0][0].tag:
                        print("{} ZZ INVALID".format(zip), flush=True)
                    else:
                        print(
                            "{} {} {}".format(
                                root[0][0].text, root[0][2].text, root[0][1].text
                            ),
                            flush=True,
                        )
                    #                    (<Element 'Zip5' at 0x7f9631e1b6d0>, '10009')
                    #                    (<Element 'City' at 0x7f9631e1b790>, 'NEW YORK')
                    #                    (<Element 'State' at 0x7f9631e1b910>, 'NY')
                    done = True
                else:
                    print(
                        "status:{} reason:{} data:{}".format(
                            resp.status, resp.reason, resp.read()
                        ),
                        flush=True,
                    )
                conn.close()
            except Exception as e:
                print("Exception:{}".format(str(e)), flush=True)
        #        time.sleep(60) # 70 days!
        time.sleep(5)  # 3 days


if "__main__" == __name__:
    srvr = "production.shippingapis.com"
    userId = os.getenv("USPSID")
    if userId:
        walk_zips(srvr, userId)
    else:
        print("set USPSID environment variable")
