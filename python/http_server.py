#!/usr/bin/env python3
import http.server
import os
import socket
import socketserver

PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        s.do_HEAD()
        s.wfile.write(
            bytes(
                "<html>\n"
                + "  <head>\n"
                + "    <title>"
                + socket.gethostname()
                + "</title>\n"
                + "  </head>\n"
                + "  <body>\n"
                + "    <p>Accessed path: {}</p>\n".format(s.path)
                + "    <p>HOME: {}</p>\n".format(os.environ["HOME"])
                + "  </body>\n"
                + "</html>\n",
                "utf8",
            )
        )


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
