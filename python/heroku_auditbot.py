#!/usr/bin/env python3

import argparse
import os
import re
import subprocess

MONEY_PATTERN = r'\$([0-9.]+)/'
ADDON_PATTERN = r'^(\S+)\s\((\S+)\)'

def get_my_email_address():
    return subprocess.check_output(['heroku', 'auth:whoami']).strip().decode(
        'utf-8'
    )

def fix_addon(expected_name, actual_name, verbose):
    print('Expected:{} Actual:{}'.format(expected_name, actual_name))
    if 'Y' == input('press "Y" to fix '):
        subprocess.check_call(['heroku', 'addons:rename',
                               actual_name, expected_name])

def get_buildpacks(app, verbose):
    buildpacks = []
    output = subprocess.check_output(['heroku', 'buildpacks', '-a', app]).decode(
        'utf-8'
    )
    if verbose > 1:
        print(output)
    if '{} has no Buildpack URL set.\n'.format(app) == output:
        return 'no buildpack set'
    for line in output.splitlines():
        if line.startswith('=== {} Buildpack URL'.format(app)):
            continue
        buildpacks.append(line)
    return ' '.join(buildpacks)

def get_apps(verbose):
    apps = []
    output = subprocess.check_output(['heroku', 'apps']).decode('utf-8')
    if verbose > 1:
        print(output)
    for line in output.splitlines():
        if (line.startswith('===') or
            line.startswith('You have no apps') or
            0 == len(line)):
            pass
        else:
            apps.append(line.split()[0]) # if there are spaces, split, take 1st
    return apps

def get_app_info(app, my_email_address, verbose):
    output = subprocess.check_output(['heroku', 'apps:info', '-a', app]).decode(
        'utf-8'
    )
    if verbose > 1:
        print(output)
    else:
        results = []
        for line in output.splitlines():
            if line.startswith('Stack'):
                (_, stack) = line.split(':')
                stack.strip()
            for word in line.split():
                if '@' in word and my_email_address != word:
                    print(word)
                    results.append(word)
        if 0 != len(results):
            print('{} has collaborators: {}'.format(app, ' '.join(results)))
    return stack.strip()

def get_addons(app, fix, verbose):
    total = 0.0
    output = subprocess.check_output(['heroku', 'addons', '-a', app]).decode(
        'utf-8'
    )
    if verbose > 1:
        print(output)
    for line in output.splitlines():
        if (line.startswith('──') or
            line.startswith('Add-on') or
            line.startswith(' ') or
            0 == len(line)):
            pass
        else:
            match = re.search(MONEY_PATTERN, line)
            if match:
                total += float(match.group(1))
            match = re.search(ADDON_PATTERN, line)
            if match:
                expected_name = match.group(1) + '-' + app
                actual_name = match.group(2)
                if expected_name != actual_name:
                    print('Add on does not follow naming convention: ' + line)
                    if fix:
                        fix_addon(expected_name, actual_name, verbose)
    return total

if '__main__' == __name__:
    grand_total = 0.0
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fix', action='store_true',
                        help='fix inconsistency if possible')
    parser.add_argument('-o', '--org',
                        help='which organization apps to audit')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='show verbose output')
    args = parser.parse_args()
    if args.org:
        os.environ['HEROKU_ORGANIZATION']=args.org
    results = []
    max_app_len = 0
    max_stack_len = 0
    max_buildpack_len = 0
    for app in get_apps(args.verbose):
        if args.verbose > 0:
            print('Checking: {}'.format(app))
        try:
            cost = get_addons(app, args.fix, args.verbose)
            stack = get_app_info(app, get_my_email_address(), args.verbose)
            buildpack = get_buildpacks(app, args.verbose)
            results.append((app, cost, stack, buildpack))
            max_app_len = max(len(app), max_app_len)
            max_stack_len = max(len(stack), max_stack_len)
            max_buildpack_len = max(len(buildpack), max_buildpack_len)
            grand_total += cost
        except:
            print('NO ACCESS:{}'.format(app))
    format_str = '{:' + str(max_app_len) + '}' + \
                 '${:8,.2f}:' +\
                 '{:' + str(max_stack_len) + '}:' +\
                 '{:' + str(max_buildpack_len) + '}'
    for (app, cost, stack, buildpack) in results:
        print(format_str.format(app, cost, stack, buildpack))

    print('-'*(max_app_len + 11 + max_stack_len + max_buildpack_len))
    print('{}${:8,.2f}'.format(' '*max_app_len, grand_total))
