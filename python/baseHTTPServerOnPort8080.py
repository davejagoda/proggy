#!/usr/bin/python

import BaseHTTPServer, CGIHTTPServer
http_server = BaseHTTPServer.HTTPServer(('',8080),CGIHTTPServer.CGIHTTPRequestHandler)
http_server.serve_forever()
