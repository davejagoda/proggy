#!/usr/bin/env python3

import os
import sys

import tweepy

tokens = ["ConsumerKey", "ConsumerSecret", "AccessTokenKey", "AccessTokenSecret"]

for token in tokens:
    if not os.getenv(token):
        print("error: set", token, "environment variable")
        sys.exit(1)

if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "<message to tweet>")
    sys.exit(1)

auth = tweepy.OAuthHandler(os.getenv("ConsumerKey"), os.getenv("ConsumerSecret"))
auth.set_access_token(os.getenv("AccessTokenKey"), os.getenv("AccessTokenSecret"))
api = tweepy.API(auth)
try:
    api.update_status(sys.argv[1])
    print("tweeted:", sys.argv[1], "as user:", api.me().name)
except:
    print("tweet failed")
