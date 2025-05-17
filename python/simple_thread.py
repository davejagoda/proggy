#!/usr/bin/env python3

# https://docs.python.org/2/library/queue.html

import argparse
import queue
import threading


def source():
    with open("/usr/share/dict/words", "r") as f:
        return [line.rstrip() for line in f.readlines()]


def do_work(word):
    if args.verbosity > 1:
        print("{}:{}".format(word, len(word)))


def worker():
    while True:
        word = q.get()
        if args.verbosity > 1:
            print(f"{threading.get_ident()} {threading.get_native_id()} got {word}")
        do_work(word)
        q.task_done()


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--thread_count", type=int, default=1)
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
if args.verbosity:
    print("thread_count:{}".format(args.thread_count))

q = queue.Queue()
for i in range(args.thread_count):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

for word in source():
    if args.verbosity > 1:
        print("raw word:{}".format(word))
    q.put(word)

q.join()  # block until all tasks are done
