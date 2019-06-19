#!/usr/bin/env python3

import subprocess

if '__main__' == __name__:
    for line in subprocess.check_output(['./subby.sh'],
                                        env={'FOO': 'bar'}).splitlines():
        print(line.decode('utf8'))
