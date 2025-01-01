#!/usr/bin/env python2

# https://www.piware.de/2011/01/creating-an-https-server-in-python/
# make self-signed cert:
# openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

import argparse
import ssl

import BaseHTTPServer
import SimpleHTTPServer


class djHTTPServer(SimpleHTTPServer.SimpleHTTPRequestHandler):
    pass


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", required=True, help="listen port")
    parser.add_argument("-s", "--ssl", action="store_true", help="SSL")
    parser.add_argument("-v", "--verbose", action="store_true", help="be verbose")
    args = parser.parse_args()
    httpd = BaseHTTPServer.HTTPServer(("", int(args.port)), djHTTPServer)
    if args.ssl:
        httpd.socket = ssl.wrap_socket(
            httpd.socket, certfile="localhost.pem", server_side=True
        )
    httpd.serve_forever()
