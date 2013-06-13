#!/usr/bin/python

import datetime

print(datetime.datetime.utcnow().replace(microsecond=0).isoformat()+'Z')




