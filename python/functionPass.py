#!/usr/bin/env python3

def function_to_pass(arg):
    print(f'inside function_to_pass({arg})')

def function_passer(arg):
    print(f'inside function_passer({arg})')
    arg('an argument from function passer')

if '__main__' == __name__:
    print('in main')
    function_passer(function_to_pass)
