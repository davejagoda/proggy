#!/usr/bin/env python

import os, sys, tweepy, time

tokens=[
    'ConsumerKey',
    'ConsumerSecret',
    'AccessTokenKey',
    'AccessTokenSecret'
    ]

for token in tokens:
    if not os.getenv(token):
        print 'error: set', token, 'environment variable'
        sys.exit(1)

if len(sys.argv) != 2:
    print 'Usage:', sys.argv[0], 'screen_name'
    sys.exit(1)

auth = tweepy.OAuthHandler(os.getenv('ConsumerKey'),
                           os.getenv('ConsumerSecret'))
auth.set_access_token(os.getenv('AccessTokenKey'),
                      os.getenv('AccessTokenSecret'))
api = tweepy.API(auth)

# this will get my tweets:
#for s in tweepy.Cursor(api.user_timeline).items():

# this well get the tweets of the user passed in
for s in tweepy.Cursor(api.user_timeline, id=sys.argv[1]).items():
    print s.id, s.text
    print
    time.sleep(5)
