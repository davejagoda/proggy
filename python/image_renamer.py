#!/usr/bin/env python

import argparse
import PIL.Image
import PIL.ExifTags
import os
import pprint
import subprocess

def openImageFile(filename):
    try:
        subprocess.call(['xdg-open', filename])
    except:
        subprocess.call(['open', filename])

def generateNameFromExif(filename, verbose):
# https://stackoverflow.com/questions/4764932/in-python-how-do-i-read-the-exif-data-for-an-image#4765242
    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in PIL.Image.open(filename)._getexif().items()
        if k in PIL.ExifTags.TAGS
    }
    if verbose > 1:
        pprint.pprint(exif)
    (date_str, time_str) = exif['DateTime'].replace(':','-').split()
    try:
        subsec =  exif['SubsecTimeOriginal']
    except KeyError:
        subsec = '000'
    camera = exif['Model'].replace(' ','_')
    return('{}T{}.{}{}.jpg'.format(date_str, time_str, subsec, camera))

def askToRename(oldName, newName, homedir):
    newPath = '{}/Documents/efoto/{}'.format(homedir, newName)
    if 'y' == input('move to {} '.format(newPath)).lower():
        if os.path.exists(newPath):
            print('path:{} already exists'.format(newPath))
            sys.exit(1)
        print('renaming')
        os.rename(oldName, newPath)
    else:
        print('leaving name unchanged')

if '__main__' == __name__:
    homedir = os.path.expanduser('~')
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True,
                        help='the file to be processed')
    parser.add_argument('-r', '--rename', action='store_true',
                        help='the file to be processed')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='show verbose output')
    args = parser.parse_args()
    if os.path.isfile(args.filename):
        newName = generateNameFromExif(args.filename, args.verbose)
        if args.verbose > 0:
            print(newName)
        openImageFile(args.filename)
        if args.rename:
            askToRename(args.filename, newName, homedir)
    else:
        print('{} not found'.format(args.filename))
