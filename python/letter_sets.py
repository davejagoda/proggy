#!/usr/bin/env python3

import string

vowels = {x for x in 'aeiou'}
first15 = {x for x in string.ascii_lowercase[:15]}
last15 = {x for x in string.ascii_lowercase[-15:]}

print('vowels & first15: {}'.format(vowels & first15))
assert vowels & first15 == {'a', 'e', 'i', 'o'}
print('vowels & last15: {}'.format(vowels & last15))
assert vowels & last15 == {'o', 'u'}
print('first15 & last15: {}'.format(first15 & last15))
assert first15 & last15 == {'l', 'm', 'n', 'o'}
