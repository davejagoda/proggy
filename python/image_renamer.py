#!/usr/bin/env python

import argparse
import PIL.Image
import PIL.ExifTags
import os
import subprocess

def openImageFile(filename):
    try:
        subprocess.call(['xdg-open', filename])
    except:
        subprocess.call(['open', filename])

def generateNameFromExif(filename):
# https://stackoverflow.com/questions/4764932/in-python-how-do-i-read-the-exif-data-for-an-image#4765242
    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in PIL.Image.open(filename)._getexif().items()
        if k in PIL.ExifTags.TAGS
    }
    (date_str, time_str) = exif['DateTime'].replace(':','').split()
    camera = exif['Model'].replace(' ','_')
    return('{}T{}00{}.jpg'.format(date_str, time_str, camera))

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
    args = parser.parse_args()
    if os.path.isfile(args.filename):
        newName = generateNameFromExif(args.filename)
        openImageFile(args.filename)
        askToRename(args.filename, newName, homedir)
    else:
        print('{} not found'.format(args.filename))
