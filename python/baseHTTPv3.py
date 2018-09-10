#!/usr/bin/env python3

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

def run(server_class=http.server.HTTPServer, handler_class=MyHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if '__main__' == __name__:
    run()
