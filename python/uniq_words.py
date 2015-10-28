#!/usr/bin/python

import sys, collections, argparse, pprint

def create_list_of_words_from_file(file):
    words = []
    with open(file, 'r') as f:
        for line in f.readlines():
            words.extend(line.strip().split())
    return(words)

def create_dict_of_uniq_words(words, verbose=False):
    uniq = {}
    for word in words:
        if verbose: print word
        if word in uniq:
            uniq[word] += 1
        else:
            uniq[word] = 1
    return(uniq)

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', help='be verbose')
    parser.add_argument('-f', '--file', help='file with words')
    parser.add_argument('words', nargs='*', help='words on the commandline')
    args = parser.parse_args()
    if args.file:
        words = create_list_of_words_from_file(args.file)
    else:
        words = []
    words.extend(args.words)
    pprint.pprint(create_dict_of_uniq_words(words, args.verbose), width=1)
