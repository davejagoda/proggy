#!/usr/bin/python

# consider a set of n words
# how many ways can you arrange them?
# numWords is the maximum number of words to be used

import itertools, argparse

def print_permutations(words, r):
    for item in itertools.permutations(words, r):
        print(''.join(item))
        print(''.join([x.title() for x in item]))

def get_list_of_words_from_file(file):
    with open(file, 'r') as f:
        return(f.read().split())

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file with words')
    parser.add_argument('-m', '--maxWords', type=int, default=0, help='maximum number of words to permute')
    parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
    args = parser.parse_args()
    if args.verbose: print(args.file)
    words = get_list_of_words_from_file(args.file)
    if args.verbose: print(words)
    if args.maxWords:
        numWords = min(len(words), args.maxWords)
    else:
        numWords = len(words)
    if args.verbose: print(numWords)
    for i in range(1, numWords+1):
        if args.verbose: print('pass:{}'.format(i))
        print_permutations(words, i)
