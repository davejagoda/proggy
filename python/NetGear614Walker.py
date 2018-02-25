#!/usr/bin/python

import sys, getopt, getpass, mechanize

def netgear_login(url, user, password):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.add_password(url, user, password)
    br.open(url)
    return br

def get_uptime(br):
    url = 'http://' + ip + '/RST_stattbl.htm'
    br.open(url)
    return br.response().read()

def get_status(br):
    url = 'http://' + ip + '/RST_status.htm'
    br.open(url)
    return br.response().read()

def get_radio(br):
    url = 'http://' + ip + '/WLG_adv.htm'
    br.open(url)
    return br.response().read()

def usage(program, ip, user, exit_status):
    print(("Usage: " + program + " [options]"))
    print("-h: display this message")
    print(("-d: IP address (default:" + ip + ")"))
    print(("-u: username (default:" + user + ")"))
    print("-p: password")
    sys.exit(exit_status)

if __name__=='__main__':
    ip = '192.168.1.1'
    user = 'admin'
    password = ''
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
    if password == '':
        password = getpass.getpass()
    print(("IP:" + ip + " User:" + user + " Password:" + password))
    url = 'http://' + ip + '/'
    br = netgear_login(url, user, password)
    print("AAA")
    print("get uptime")
    print((get_uptime(br)))
    print("get status")
    print((get_status(br)))
    print("get radio")
    print((get_radio(br)))
    print("ZZZ")
