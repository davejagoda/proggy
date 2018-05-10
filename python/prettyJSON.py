#!/usr/bin/env python3

import sys, json

for file in sys.argv[1:]:
    with open(file, 'r') as f:
        print('file: {}'.format(file))
        print(json.dumps(json.loads(f.read()), indent=2, sort_keys=True))
        print()
