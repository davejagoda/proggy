#!/usr/bin/env python3

# https://stackoverflow.com/questions/2846653/how-do-i-use-threading-in-python

import argparse
import requests
from multiprocessing.dummy import Pool as ThreadPool

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--threads', required=True, type=int)
parser.add_argument('-a', '--amplification', required=True, type=int)
args = parser.parse_args()

seed_urls = [
    'https://davejagoda.nfshost.com/perl.cgi',
    'https://davejagoda.nfshost.com/php.cgi',
    'https://davejagoda.nfshost.com/python.cgi',
]

urls = seed_urls * args.amplification

# Make the Pool of workers
pool = ThreadPool(args.threads)

# Open the URLs in their own threads
# and return the results
results = pool.map(requests.get, urls)

# Close the pool and wait for the work to finish
pool.close()
pool.join()

for result in results:
    print(f'{result.status_code} {result.text}')
