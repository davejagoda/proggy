#!/usr/bin/env python3

# must answer
# GET, HEAD, POST
# nice to have
# PUT, DELETE, TRACE, CONNECT
# http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html

# client will send stuff like this:
# Host: localhost:8888
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:40.0) Gecko/20100101 Firefox/40.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate

import argparse
import ssl
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler


class djHTTPServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        print("get")
        response = self.path + "\nClientHeaders\n" + str(self.headers)
        self.send_response(200)
        self.send_header("Content-Type", "text")
        self.send_header("Content-Length", len(response))
        self.end_headers()
        self.wfile.write(response.encode())

    def do_HEAD(self):
        print("head")
        self.send_response(200)
        self.send_header("Content-Type", "text")
        self.end_headers()

    def send_head(self, length):
        self.send_response(200)
        self.send_header("Content-Type", "text")
        self.send_header("Content-Length", length)
        self.end_headers()

    def log_date_time_string(self):
        """Overridden: Return the current time formatted for logging."""
        now = time.time()
        year, month, day, hh, mm, ss, x, y, z = time.gmtime(now)
        s = "%04d-%02d-%02dT%02d:%02d:%02dZ" % (year, month, day, hh, mm, ss)
        return s

    def log_request(self, code):
        print(code)
        print(self.raw_requestline)
        print(self.headers)
        return code


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", required=True, type=int, help="listen port")
    parser.add_argument("-s", "--ssl", action="store_true", help="SSL")
    parser.add_argument("-v", "--verbose", action="store_true", help="be verbose")
    args = parser.parse_args()
    with HTTPServer(("", args.port), djHTTPServer) as httpd:
        if args.ssl:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(certfile="localhost.pem")
            context.check_hostname = False
            httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        httpd.serve_forever()
