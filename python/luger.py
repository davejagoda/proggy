#!/usr/bin/env python3

# consider a set of n words
# how many ways can you arrange them?
# numWords is the maximum number of words to be used

import itertools, argparse

trans_table = {
    'o': ['0'],
    'i': ['1', '!'],
    'a': ['@'],
    's': ['$'],
    'e': ['3']
}

# walk each word
# at each position, try all the transforms in the dictionary
# as you generate each, call the wordwalker again from the new position
# (so that all current positions are preserved)

def walk_word(results, word, index, debug=False):
    if len(word) == index:
        if debug: print('done with this pass, result is:{}'.format(word))
        results.append(word)
        return
    w = word[index] # just to save typing
    if w in trans_table:
        if debug: print('found in trans_table')
        for value in trans_table[w]:
            new_word =  word[:index] + value + word[index+1:]
            if debug: print('value:{} new_word:{}'.format(value, new_word))
            walk_word(results, new_word, index + 1, debug)
    walk_word(results, word, index + 1, debug)

def expand_list_of_words(words):
    words.extend([x.title() for x in words])
    return(words)
#    integrate this code:
#    results = []
#    walk_word(results, word, 0, debug=False)
#    print(results)

def print_permutations(words, r):
    for item in itertools.permutations(words, r):
        print(''.join(item))

def get_list_of_words_from_file(file):
    with open(file, 'r') as f:
        return([x.lower() for x in f.read().split()])

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file with words')
    parser.add_argument('-m', '--maxWords', type=int, default=0, help='maximum number of words to permute')
    parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
    args = parser.parse_args()
    if args.verbose: print(args.file)
    words = get_list_of_words_from_file(args.file)
    assert(list == type(words))
    if args.verbose: print(words)
    words = expand_list_of_words(words)
    if args.verbose: print(words)
    if args.maxWords:
        numWords = min(len(words), args.maxWords)
    else:
        numWords = len(words)
    if args.verbose: print(numWords)
    for i in range(1, numWords+1):
        if args.verbose: print('pass:{}'.format(i))
        print_permutations(words, i)
