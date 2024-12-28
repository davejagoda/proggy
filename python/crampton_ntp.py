#!/usr/bin/env python3

# http://blog.mattcrampton.com/post/88291892461/query-an-ntp-server-from-python

from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct
import time
import datetime


def iso8601(epoch):
    return datetime.datetime.fromtimestamp(epoch).isoformat() + "Z"


def getMyTime():
    return time.time()


def getNTPTime(host="pool.ntp.org"):
    port = 123
    buf = 1024
    address = (host, port)
    msg = b"\x1b" + 47 * b"\0"

    # reference time (in seconds since 1900-01-01 00:00:00)
    TIME1970 = 2208988800  # 1970-01-01 00:00:00

    # connect to server
    client = socket.socket(AF_INET, SOCK_DGRAM)
    client.sendto(msg, address)
    msg, address = client.recvfrom(buf)

    t = struct.unpack("!12I", msg)[10] + float(struct.unpack("!12I", msg)[11]) / 2**32
    t -= TIME1970
    return t


if __name__ == "__main__":
    times = []
    times.append(["loc", getMyTime()])
    times.append(["ntp", getNTPTime()])
    times.append(["loc", getMyTime()])
    t_prev = times[0][1]
    for d, t in times:
        print("{}:{}".format(d, iso8601(t)))
        # print(t - t_prev)
        assert t - t_prev >= 0
        t_prev = t
