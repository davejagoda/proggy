#!/usr/bin/python

import subprocess, os, getpass

DEVNULL = open(os.devnull, 'wb')

pswd = getpass.getpass()
try:
    subprocess.check_call(['ssh-keygen', '-y', '-f', os.getenv('HOME') + '/.ssh/id_rsa', '-P', pswd], stdout=DEVNULL, stderr=DEVNULL)
    print('that was it!')
except:
    print('wrong password')
