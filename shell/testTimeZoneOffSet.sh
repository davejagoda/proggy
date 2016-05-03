#!/bin/sh

date -R
~/src/github/proggy/python/getTimeZoneOffSet.py

export TZ=Singapore
date -R
~/src/github/proggy/python/getTimeZoneOffSet.py

export TZ=Pacific/Nauru
date -R
~/src/github/proggy/python/getTimeZoneOffSet.py

export TZ=America/Los_Angeles
date -R
~/src/github/proggy/python/getTimeZoneOffSet.py
