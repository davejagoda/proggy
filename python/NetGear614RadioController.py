#!/usr/bin/python

import sys, getopt, getpass, mechanize, re, time

def netgear_login(url, user, password):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.add_password(url, user, password)
    br.open(url)
    return br

def get_uptime(br):
    url = "http://" + ip + "/RST_stattbl.htm"
    br.open(url)
    r = br.response().read(), "\n"
    p = re.search(r"System Up Time\D+<!>(.*)<!>", r[0])
    return p.group(1)

def get_radio_state(br):
# returns '0' for off and '1' for on
    url = "http://" + ip + "/WLG_adv.htm"
    br.open(url)
    form = mechanize.ParseResponse(br.response())[0]
    radio_control = form.find_control("enable_ap")
    return len(radio_control.value)

def set_radio_state(br, new_state):
# new_state must be '0' for off and '1' for on
    assert ( new_state == 0 or new_state == 1)
    if get_radio_state(br) == new_state:
        print "current state == new state, not changing anything"
        return

    br.select_form(nr=0)
    radio_control = br.form.find_control("enable_ap")
    radio_control.items[0].selected = new_state
#    print "control is now", br.form.find_control("enable_ap")
#    print radio_control, ':', radio_control.type, ':', radio_control.value
    response = br.submit()
    print response.code
    time.sleep(1)
    return

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
#    print "IP:" + ip + " User:" + user + " Password:" + password
    url = "http://" + ip + "/"
    br = netgear_login(url, user, password)
    print get_uptime(br)
# toggle radio state
    print "\nradio is", "on" if get_radio_state(br) else "off"
    print get_uptime(br)
    set_radio_state(br, not get_radio_state(br))
    print "\nradio is", "on" if get_radio_state(br) else "off"
    print get_uptime(br)
