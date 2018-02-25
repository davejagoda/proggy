#!/usr/bin/env python

import argparse
import os

vhost_template = '''<VirtualHost *:{1}>
    ServerName {0}
    DocumentRoot "/var/www/vhosts/{0}"
    <Directory "/var/www/vhosts/{0}">
        Options Indexes FollowSymLinks MultiViews
        AllowOverride All
    </Directory>
    CustomLog "/var/log/httpd/{0}-access.log" combined
    ErrorLog "/var/log/httpd/{0}-error.log"
    LogLevel warn
</VirtualHost>
'''

def write_vhost_conf(server_name, port, destination_directory):
    full_path = '{0}/{1}.conf'.format(destination_directory, server_name)
    if os.path.isfile(full_path):
        return('file {0} exists, not overwriting'.format(full_path))
    with open(full_path, 'w') as f:
        f.write(vhost_template.format(server_name, port))
        return('file {0} created'.format(full_path))
    return('something unexpected happened')

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('server_names', nargs='+',
                        help='the list of vhost server names to create')
    parser.add_argument('-p', '--port', default=80)
    parser.add_argument('-d', '--destination_directory', default='/tmp/vhost.d')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    for server_name in args.server_names:
        if args.verbose:
            print(server_name)
        print((write_vhost_conf(server_name, args.port, args.destination_directory)))
