#!/usr/bin/python

import argparse, os

def build_dictionary_of_known_zip_codes():
    home = os.path.expanduser('~')
    zip_file = '{}/src/github/davejagoda.github.io/data/zip_codes.md'.format(home)
    zip_dict = {}
    with open(zip_file, 'r') as f:
        for line in f.readlines():
            if 5 == len(line.split('|')):
                (bol, zip5, state, city, eol) = line.split('|')
                assert zip5 not in zip_dict
                zip_dict[zip5] = (state, city.strip())
    return zip_dict

def process_file(filename, zip_dict, verbose=False):
    exception_line_count = 0
    invalid_line_count = 0
    valid_line_count = 0
    with open(args.filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('Exception:'):
                if verbose: print(line)
                exception_line_count += 1
                continue
            terms = line.split()
            zip5, state, city = terms[0], terms[1], ' '.join(terms[2:])
            assert 5 == len(zip5)
            assert 2 == len(state)
            if 'ZZ' == state and 'INVALID' == city:
                invalid_line_count += 1
                continue
            valid_line_count += 1
            if zip_dict[zip5] != (state, city):
                print('mismatch: current:{} {} new:{} {}'.format(
                    zip_dict[zip5][0], zip_dict[zip5][1], state, city))
    print('exceptions:{} invalid:{} valid:{} valid+invalid:{}'.format(
        exception_line_count, invalid_line_count, valid_line_count,
        invalid_line_count + valid_line_count))

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    zip_dict = build_dictionary_of_known_zip_codes()
    if args.verbose:
        print('file:{}'.format(args.filename))
    process_file(args.filename, zip_dict, args.verbose)
