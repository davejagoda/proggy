#!/usr/bin/env python3

# brute force 3x3 magic square
# more clever solutions are here:
# https://puzzling.stackexchange.com/questions/1957/puzzle-of-putting-numbers-1-9-in-3x3-grid-to-add-up-to-15

def valid_number(i):
    s = str(i)
    if '123456789' == ''.join(sorted(s)):
        return True
    return False

def cols_eq_15(i):
    s = str(i)
    if (
            15 == int(s[0]) + int(s[3]) + int(s[6]) and
            15 == int(s[1]) + int(s[4]) + int(s[7]) and
            15 == int(s[2]) + int(s[5]) + int(s[8])
    ):
        return True
    return False

def rows_eq_15(i):
    s = str(i)
    if (
            15 == int(s[0]) + int(s[1]) + int(s[2]) and
            15 == int(s[3]) + int(s[4]) + int(s[5]) and
            15 == int(s[6]) + int(s[7]) + int(s[8])
    ):
        return True
    return False

def diags_eq_15(i):
    s = str(i)
    if (
            15 == int(s[0]) + int(s[4]) + int(s[8]) and
            15 == int(s[6]) + int(s[4]) + int(s[2])
    ):
        return True
    return False

for i in range(123456789, 987654321+1):
    if valid_number(i):
#        print(f'valid: {i}')
        if cols_eq_15(i):
#            print(f'cols: {i}')
            if rows_eq_15(i):
#                print(f'rows: {i}')
                if diags_eq_15(i):
                    print(f'diags: {i}')
