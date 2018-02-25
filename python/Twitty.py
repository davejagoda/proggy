#!/usr/bin/python
import random

witticisms = ['foo','bar','baz']

while len(witticisms) > 0:
    print((witticisms.pop(random.randrange(len(witticisms)))))
