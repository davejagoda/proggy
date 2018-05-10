#!/usr/bin/env python3

# trying to do something like this in a less brittle way:
#last | grep dj | cut -b 23-38 | sort | uniq -c

import subprocess, getpass, json, argparse, os, datetime

def process_line(line, places):
    words = line.split()
    if words and getpass.getuser() == words[0]:
        if words[2] in places:
            places[words[2]] += 1
        else:
            places[words[2]] = 1

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='show verbose output')
    args = parser.parse_args()
    if args.verbose:
        print('about to begin')
    json_file_path = '{}/whereDoIComeFrom.json'.format(os.path.expanduser('~'))
    if os.path.isfile(json_file_path):
        print('updating existing JSON file')
        with open(json_file_path, 'r') as f:
            places = json.loads(f.read())
    else:
        print('creating JSON file')
        places = {}
    stdout = subprocess.check_output(['last'])
    lines = stdout.splitlines()
    for line in lines:
        process_line(line, places)
    print(json.dumps(places, indent=2))
    new_json_file_path = '{}.{}'.format(json_file_path,
                                        datetime.datetime.utcnow().replace(
                                            microsecond=0).isoformat()+'Z')
    with open(new_json_file_path, 'w') as f:
        json.dump(places, f)
