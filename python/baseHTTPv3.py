#!/usr/bin/env python3

# https://wiki.python.org/moin/BaseHttpServer#Example_Code

import argparse
import datetime
import http.server
import socket
import time


class MyHandler(http.server.BaseHTTPRequestHandler):

    def send_headers(self):
        if self.server.delay > 0:
            time.sleep(self.server.delay)
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.send_headers()
        self.wfile.write(
            bytes(
                "<html>\n"
                + "  <head>\n"
                + "    <title>"
                + socket.gethostname()
                + "</title>\n"
                + "  </head>\n"
                + "  <body>"
                + datetime.datetime.utcnow().isoformat()
                + "</body>\n"
                + "</html>\n",
                "utf-8",
            )
        )

    def do_HEAD(self):
        self.send_headers()


def run(server_class, handler_class, server_port, delay):
    server_address = ("", server_port)
    httpd = server_class(server_address, handler_class)
    httpd.delay = delay
    print(
        "httpd listening on port {} with a {} second delay".format(server_port, delay)
    )
    httpd.serve_forever()


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--delay", type=int, default=0, help="delay in seconds before responding"
    )
    parser.add_argument(
        "--port", type=int, default=8000, help="listen to this port for HTTP requests"
    )
    args = parser.parse_args()
    run(http.server.HTTPServer, MyHandler, args.port, args.delay)
