#!/usr/bin/python

import sys, getopt, getpass, urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse, re, base64

def get_radio_state(ip, user, password):
# returns "0" for off and "1" for on
    url = "http://" + ip + "/WLG_adv.htm"
    b64login = base64.b64encode(user + ":" + password)
    req = urllib.request.Request(url)
    req.add_header("Authorization", "Basic " + b64login)
    res = urllib.request.urlopen(req)
    assert (200 == res.getcode())
    body = res.read()
#OFF:
#<input type="checkbox"   name="enable_ap" value="enable_ap"> Enable Wireless Router Radio
#ON:
#<input type="checkbox"  checked name="enable_ap" value="enable_ap"> Enable Wireless Router Radio
    pat = re.search(r'"checkbox"(.*)name="enable_ap"', body)
# this will be "checked" if radio is enabled, else radio disabled
    assert (None != pat)
    if (re.search(r'checked', pat.group(1))):
        return 1
    else:
        return 0

def set_radio_state(ip, user, password, new_state):
# new_state must be "0" for off and "1" for on
    assert ( 0 == new_state or 1 == new_state)
    if get_radio_state(ip, user, password) == new_state:
        print("current state == new state, not changing anything")
        return
    url = "http://" + ip + "/wlgadv.cgi"
    b64login = base64.b64encode(user + ":" + password)
    req = urllib.request.Request(url)
    req.add_header("Authorization", "Basic " + b64login)
    dict = {"ssid_bc": "ssid_bc", "Apply": "Apply", "blankstate": "0"}
    if new_state:
        dict["enable_ap"] = "enable_ap"
#    data = urllib.urlencode(dict)
    res = urllib.request.urlopen(req, urllib.parse.urlencode(dict))
    assert (200 == res.getcode())
    return

def usage(program, ip, user, exit_status):
    print(("Usage: " + program + " [options]"))
    print("-h: display this message")
    print(("-d: IP address (default:" + ip + ")"))
    print(("-u: username (default:" + user + ")"))
    print("-p: password")
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
#    print "IP:" + ip + " User:" + user + " Password:" + password
    print(("radio is", "on" if get_radio_state(ip, user, password) else "off"))
# toggle radio state
    set_radio_state(ip, user, password, not get_radio_state(ip, user, password))
    print(("radio is", "on" if get_radio_state(ip, user, password) else "off"))
