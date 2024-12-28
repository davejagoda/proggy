#!/usr/bin/env python3

import sys, smtplib

assert 2 == len(sys.argv), "provide email address as an argument"
addr = sys.argv[1]
m = "To: " + addr + "\n"
m += "From: " + addr + "\n"
m += "Subject: test from " + sys.argv[0] + "\n"
m += "Hi\n"

s = smtplib.SMTP("localhost")
s.sendmail(addr, [addr], m)
s.quit()
