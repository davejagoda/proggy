#!/usr/bin/python

import sys, getopt, getpass, mechanize

def netgear_login(url, user, password):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.add_password(url, user, password)
    br.open(url)
    return br

def get_uptime(br):
#   url = 'http://' + ip + '/RST_statistics.htm'
    return -1

def get_radio_state(br):
    forms = mechanize.ParseResponse(br.response())
    form = forms[0]
#    print form
    radio_control = form.find_control("enable_ap")
#    print radio_control.value
    if len(radio_control.value):
        return True
    else:
        return False

def set_radio_state(br, state):
    # state must be True or False
    if get_radio_state(br) == state:
        return
    forms = mechanize.ParseResponse(br.response())
    form = forms[0]
#    print form
    radio_control = form.find_control("enable_ap")
    radio_control.items[0].selected = state
    print form.find_control("enable_ap")
# unauth?
#    request = form.click()
#    mechanize.urlopen(request)
    radio_control.click()
    return

def usage(program, ip, user, exit_status):
    print "Usage: " + program + " [options]"
    print "-h: display this message"
    print "-d: IP address (default:" + ip + ")"
    print "-u: username (default:" + user + ")"
    print "-p: password"
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
#    print "IP:" + ip + " User:" + user + " Password:" + password
    url = 'http://' + ip + '/WLG_adv.htm'
    br = netgear_login(url, user, password)
#    print br.response().read()
    if get_radio_state(br):
        print "radio is on"
    else:
        print "radio is off"

    set_radio_state(br, False)

    if get_radio_state(br):
        print "radio is on"
    else:
        print "radio is off"

#    print get_uptime(br)
