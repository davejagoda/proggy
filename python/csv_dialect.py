#!/usr/bin/env python3

import csv

dialect_attrs = [
    'delimiter',
    'doublequote',
    'escapechar',
    'lineterminator',
    'quotechar',
    'quoting',
    'skipinitialspace',
    'strict'
]

def replace_class(o):
    if isinstance(o, str):
        return o
    return str(o)

def replace_chars(s):
    return s.replace('\t', '\\t').replace('\n', '\\n').replace('\r', '\\r')

max_field = 0
corned_beef = {}
for dialect in csv.list_dialects():
    max_field = max(max_field, len(dialect))
    corned_beef[dialect] = {}
    d = csv.get_dialect(dialect)
    found_dialects = []
    for name in dir(d):
        max_field = max(max_field, len(name))
        if name.startswith('__') and name.endswith('__'):
            continue
        found_dialects.append(name)
        value = getattr(d, name)
        value = replace_class(value)
        max_field = max(max_field, len(value))
        value = replace_chars(value)
        corned_beef[dialect][name] = value
    assert set(dialect_attrs) == set(found_dialects)

print(' ' * max_field, end='')
for key in corned_beef:
    print(f'{key:>{max_field}}', end='')
print()
for attr in dialect_attrs:
    print(f'{attr:>{max_field}}', end='')
    for key in corned_beef:
        print(f'{corned_beef[key][attr]:>{max_field}}', end='')
    print()
