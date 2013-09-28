#!/usr/bin/python

import BaseHTTPServer, CGIHTTPServer, time

class djHTTPServer(CGIHTTPServer.CGIHTTPRequestHandler):
    def log_date_time_string(self):
        """Overridden: Return the current time formatted for logging."""
        now = time.time()
        year, month, day, hh, mm, ss, x, y, z = time.gmtime(now)
        s = "%04d-%02d-%02dT%02d:%02d:%02dZ" % (
                year, month, day, hh, mm, ss)
        return s

import BaseHTTPServer, CGIHTTPServer
Handler_Class = djHTTPServer
httpd = BaseHTTPServer.HTTPServer(('',8080), Handler_Class)
httpd.serve_forever()

