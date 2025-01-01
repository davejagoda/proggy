#!/usr/bin/env python3

import argparse
import operator


def create_list_of_words_from_file(file):
    words = []
    with open(file, "r") as f:
        for line in f.readlines():
            words.extend(line.strip().split())
    return words


def create_dict_of_uniq_words(words):
    uniq = {}
    for word in words:
        if word in uniq:
            uniq[word] += 1
        else:
            uniq[word] = 1
    return uniq


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="file with words")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-k", "--keysort", action="store_true", help="sort based on key")
    group.add_argument(
        "-v", "--valsort", action="store_true", help="sort based on value"
    )
    parser.add_argument("words", nargs="*", help="words on the commandline")
    args = parser.parse_args()
    if args.file:
        words = create_list_of_words_from_file(args.file)
    else:
        words = []
    words.extend(args.words)
    dict = create_dict_of_uniq_words(words)
    if not args.keysort and not args.valsort:
        for k, v in dict.items():
            print("{}: {}".format(k, v))
    if args.keysort:
        for k, v in sorted(dict.items(), key=(operator.itemgetter(0))):
            print("{}: {}".format(k, v))
    if args.valsort:
        for k, v in sorted(dict.items(), key=(operator.itemgetter(1, 0))):
            print("{}: {}".format(k, v))
