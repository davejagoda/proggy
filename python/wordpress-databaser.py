#!/usr/bin/env python

# given a directory full of unzipped wordpress installs
# e.g. from wordpress-unzipper-configurator.py
# create corresponding MySQL databases like this wordpress-x.y.z

import argparse, os, subprocess

def create_wordpress_database(db_name, verbose):
    subprocess.check_output(['mysqladmin', '-u', 'root', 'create', db_name])

def drop_wordpress_database(db_name, verbose):
    subprocess.check_output(['mysqladmin', '-u', 'root', '-f', 'drop', db_name])

def process_directory(src, dropDatabase, verbose):
    assert(os.path.isdir(src))
    assert(os.path.exists(os.path.expanduser('~/.my.cnf')))
    for root, dirs, filenames in os.walk(src):
        for dir_name in dirs:
            if verbose > 0:
                print('about to process {}'.format(dir_name))
            if dropDatabase:
                drop_wordpress_database(dir_name, verbose)
            else:
                create_wordpress_database(dir_name, verbose)
        break # only want the first level of directories

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', help='show verbose output')
    parser.add_argument('-s', '--src', help='directory of unzipped wordpress installs', required=True)
    parser.add_argument('--dropDatabase', action='store_true', help='drop all matching databases, very dangerous!')
    args = parser.parse_args()
    process_directory(args.src, args.dropDatabase, args.verbose)
