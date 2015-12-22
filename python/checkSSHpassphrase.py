#!/usr/bin/python

import subprocess, os, getpass

DEVNULL = open(os.devnull, 'wb')

def validate_password(pswd):
    try:
        subprocess.check_call(['ssh-keygen', '-y', '-f', os.getenv('HOME') + '/.ssh/id_rsa', '-P', pswd], stdout=DEVNULL, stderr=DEVNULL)
        return(True)
    except:
        return(False)

if '__main__' == __name__:
    pswd = getpass.getpass()
    if validate_password(pswd):
        print('that was it!')
    else:
        print('wrong password')
