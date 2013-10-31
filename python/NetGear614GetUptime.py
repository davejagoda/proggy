#!/usr/bin/python

import sys, getopt, getpass, urllib2, re, base64

def get_uptime(url, user, password):
    b64login = base64.b64encode("%s:%s" % (user, password))
    req = urllib2.Request(url)
    req.add_header("Authorization", "Basic " + b64login )
    res = urllib2.urlopen(req)
    body = res.read()
    p = re.search(r"System Up Time\D+<!>(.*)<!>", body)
    return p.group(1)

def usage(program, ip, user, exit_status):
    print "Usage: " + program + " [options]"
    print "-h: display this message"
    print "-d: IP address (default:" + ip + ")"
    print "-u: username (default:" + user + ")"
    print "-p: password"
    sys.exit(exit_status)

if __name__=="__main__":
    ip = "192.168.1.1"
    user = "admin"
    password = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:u:p:", [])
    except getopt.GetoptError:
        usage(sys.argv[0], ip, user, 1)
    for opt, arg in opts:
        if opt == "-h":
            usage(sys.argv[0], ip, user, 0)
        if opt == "-d":
            ip = arg
        if opt == "-u":
            user = arg
        if opt == "-p":
            password = arg
    if password == "":
        password = getpass.getpass()
    url = "http://" + ip + "/RST_stattbl.htm"
    print get_uptime(url, user, password)
