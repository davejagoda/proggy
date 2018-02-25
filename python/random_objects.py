#!/usr/bin/env python

import random

class RandomClass:
    """A class with random objects"""
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
    def __repr__(self):
        return('name:{} rank:{}'.format(self.name, self.rank))

def random_generator():
    ranks = list(range(10))
    objects = []
    while ranks:
        selected = ranks.pop(random.randrange(len(ranks)))
        objects.append(RandomClass(chr(65+selected), selected))
    while objects:
        yield(objects.pop(random.randrange(len(objects))))

if __name__ == '__main__':
    min_id = 0
    for o in sorted([o for o in random_generator()]):
        print(('id:{} {}'.format(id(o), o)))
        assert(min_id < id(o))
        min_id = id(o)
