#!/usr/bin/python

import sys, getopt, getpass, mechanize, re, base64

def get_uptime(url, user, password):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.add_password(url, user, password)
    print br.open(url).code
    r = br.response().read()
    p = re.search(r"System Up Time\D+<!>(.*)<!>", r)
    return p.group(1)

def get_uptime_no_401(url, user, password):
    b64login = base64.b64encode("%s:%s" % (user, password))
    br = mechanize.Browser()
    br.addheaders.append(("Authorization", "Basic " + b64login ))
    print br.open(url).code
    r = br.response().read()
    p = re.search(r"System Up Time\D+<!>(.*)<!>", r)
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
    print get_uptime_no_401(url, user, password)

# why we are making one authed then one unauthed request?
