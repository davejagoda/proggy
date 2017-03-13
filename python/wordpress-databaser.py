#!/usr/bin/env python

# given a directory full of unzipped wordpress installs
# e.g. from wordpress-unzipper-configurator.py
# create corresponding MySQL databases like this wordpress-x.y.z

import argparse, os, subprocess

def create_wordpress_database(db_name, verbose):
    subprocess.check_output(['mysqladmin', '-u', 'root', 'create', db_name])
    db_command = 'GRANT ALL PRIVILEGES ON {0}.* TO "{0}"@"localhost" IDENTIFIED BY "{0}";'.format(db_name)
    if verbose > 0:
        print(db_command)
    p1 = subprocess.Popen(['echo', db_command], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['mysql', '-uroot', db_name], stdin=p1.stdout)

def drop_wordpress_database(db_name, verbose):
    subprocess.check_output(['mysqladmin', '-u', 'root', '-f', 'drop', db_name])

def process_directory(src, dropDatabase, verbose):
    assert(os.path.isdir(src))
    assert(os.path.exists(os.path.expanduser('~/.my.cnf')))
    for root, dirs, filenames in os.walk(src):
        for dir_name in dirs:
            if verbose > 0:
                print('about to process {}'.format(dir_name))
            db_name = dir_name.replace('-','_') # convert '-' to '_' to reduce quoting in MySQL
            db_name = db_name.replace('.','_') # convert '.' to '_' to reduce quoting in MySQL
            if dropDatabase:
                drop_wordpress_database(db_name, verbose)
            else:
                create_wordpress_database(db_name, verbose)
        break # only want the first level of directories

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='increase output verbosity')
    parser.add_argument('-s', '--src', help='directory of unzipped wordpress installs', required=True)
    parser.add_argument('--dropDatabase', action='store_true', help='drop all matching databases, very dangerous!')
    args = parser.parse_args()
    process_directory(args.src, args.dropDatabase, args.verbose)
