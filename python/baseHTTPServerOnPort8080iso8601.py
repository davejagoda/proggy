#!/usr/bin/env python2

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
import BaseHTTPServer
import SimpleHTTPServer
import time


class djHTTPServer(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("get")
        response = self.path + "\nClientHeaders\n" + str(self.headers)
        print(dir(self.headers))
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.send_header("Content-Length", len(response))
        self.end_headers()
        #        self.send_head(len(response))
        self.wfile.write(response)

    def do_HEAD(self):
        print("head")
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()

    #        response = self.path# + self.headers
    #        self.send_head(len(response))

    def send_head(self, length):
        self.send_response(200)
        self.send_header("Content-type", "text")
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
        print(dir(self))
        print(self.raw_requestline)
        print(self.headers)
        return code


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
