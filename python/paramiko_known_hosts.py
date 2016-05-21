#!/usr/bin/env python

import paramiko, os, argparse

def host_connect(ssh, user, host):
    ssh.connect(host, username=user)
    stdin, stdout, stderr = ssh.exec_command('whoami && uname -n')
    return('@'.join(x.strip() for x in stdout.readlines()))

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('remote', nargs='+', help='[user@]host ...')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    paramiko.util.log_to_file('ssh.log')
    ssh = paramiko.SSHClient()
    ssh_key_file = '{}/.ssh/known_hosts'.format(os.path.expanduser('~'))
    ssh.load_host_keys(ssh_key_file)

    for remote in args.remote:
        if '@' in remote:
            (user, host) = remote.split('@')
        else:
            user = None
            host = remote
        if args.verbose:
            print('{}@{}'.format(user, host))
        print(host_connect(ssh, user, host))
