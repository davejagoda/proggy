#!/usr/bin/env python3

# given a directory full of a bunch of wordpress zip files
# like this wordpress-2.0.1.zip
# they will by default unzip into a wordpress directory
# upon unzipping, rename that directory to wordpress-x.y.z
# in each unzipped directory, create wp-config.php from wp-config-sample.php

import argparse, os, subprocess

def process_wordpress_directory(new_dir_name, basename, verbose):
    wp_config        = os.path.join(new_dir_name, 'wp-config.php')
    wp_config_sample = os.path.join(new_dir_name, 'wp-config-sample.php')
    assert(not os.path.exists(wp_config))
    assert(os.path.isfile(wp_config_sample))
    db_name = basename.replace('-','_') # convert '-' to '_' to reduce quoting in MySQL
    db_name = db_name.replace('.','_') # convert '.' to '_' to reduce quoting in MySQL
    with open(wp_config_sample, 'r') as org_f:
        with open(wp_config, 'w') as new_f:
            for line in org_f:
                if line.startswith("define('DB_NAME'"):
                    line = "define('DB_NAME', '{}');\r\n".format(db_name)
                if line.startswith("define('DB_USER'"):
                    line = "define('DB_USER', '{}');\r\n".format(db_name)
                if line.startswith("define('DB_PASSWORD'"):
                    line = "define('DB_PASSWORD', '{}');\r\n".format(db_name)
                new_f.write(line)

def process_zip(zip_file_name, src, dst, verbose):
    zip_file_with_path = os.path.join(src, zip_file_name)
    assert(os.path.isfile(zip_file_with_path))
    basename, extension = os.path.splitext(zip_file_name)
    assert('.zip' == extension)
    subprocess.check_output(['unzip', zip_file_with_path, '-d', dst])
    org_dir_name = os.path.join(dst, 'wordpress')
    new_dir_name = os.path.join(dst, basename)
    assert(os.path.isdir(org_dir_name))
    os.rename(org_dir_name, new_dir_name)
    return(new_dir_name, basename)

def process_directory(src, dst, verbose):
    assert(os.path.isdir(src))
    assert(not os.path.exists(dst))
    for root, dirs, filenames in os.walk(src):
        for filename in filenames:
            if verbose > 0:
                print('about to process {}'.format(filename))
            new_dir_name, basename = process_zip(filename, root, dst, verbose)
            if verbose > 0:
                print('about to process directory {}'.format(new_dir_name))
            process_wordpress_directory(new_dir_name, basename, verbose)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='increase output verbosity')
    parser.add_argument('-s', '--src',  required=True,
                        help='directory full of zip files')
    parser.add_argument('-d', '--dst', required=True,
                        help='directory in which to unzip')
    args = parser.parse_args()
    process_directory(args.src, args.dst, args.verbose)
