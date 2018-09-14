#!/usr/bin/env python3

# https://wiki.python.org/moin/BaseHttpServer#Example_Code

import argparse
import datetime
import http.server
import socket

class MyHandler(http.server.BaseHTTPRequestHandler):

    def send_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.send_headers()
        self.wfile.write(bytes(
            '<html>\n' +
            '  <head>\n' +
            '    <title>' + socket.gethostname() + '</title>\n' +
            '  </head>\n' +
            '  <body>' + datetime.datetime.utcnow().isoformat() + '</body>\n' +
            '</html>\n', 'utf-8'))

    def do_HEAD(self):
        self.send_headers()

def run(server_class, handler_class, server_port):
    server_address = ('', server_port)
    httpd = server_class(server_address, handler_class)
    print('httpd listening on port:{}'.format(server_port))
    httpd.serve_forever()

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000,
                        help='listen to this port for HTTP requests')
    args = parser.parse_args()
    run(http.server.HTTPServer, MyHandler, args.port)
