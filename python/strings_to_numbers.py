#!/usr/bin/env python3

list_of_inputs = [
    '0',
    '1',
    ' 2',
    '3 ',
    'a',
    'g',
    '',
    'tbd',
    '8',
    '9'
]

for item in list_of_inputs:
    print(f'{item} ', end='')
    try:
        print(int(item))
    except ValueError:
        print(f'could not convert {item} to an integer')
