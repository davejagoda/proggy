#!/usr/bin/env python3

# https://www.piware.de/2011/01/creating-an-https-server-in-python/
# make self-signed cert:
# openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes

import argparse
import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", required=True, type=int, help="listen port")
    parser.add_argument("-s", "--ssl", action="store_true", help="SSL")
    parser.add_argument("-v", "--verbose", action="store_true", help="be verbose")
    args = parser.parse_args()
    with HTTPServer(("", args.port), SimpleHTTPRequestHandler) as httpd:
        if args.ssl:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(certfile="localhost.pem")
            context.check_hostname = False
            httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        httpd.serve_forever()
