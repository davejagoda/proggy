#!/usr/bin/env python3

# https://docs.python.org/2/library/queue.html

import argparse
import queue
import threading


def source():
    with open("/usr/share/dict/words", "r") as f:
        return [line.rstrip() for line in f.readlines()]


def do_work(item):
    print("{}:{}".format(item, len(item)))


def worker():
    while True:
        item = q.get()
        if args.verbose:
            print(f'{threading.get_ident()} {threading.get_native_id()} got {item}')
        do_work(item)
        q.task_done()


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--thread_count", type=int, default=1)
parser.add_argument("-v", "--verbose", default=False, action="store_true")
args = parser.parse_args()
if args.verbose:
    print("thread_count:{}".format(args.thread_count))

q = queue.Queue()
for i in range(args.thread_count):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

for item in source():
    if args.verbose:
        print("raw item:{}".format(item))
    q.put(item)

q.join()  # block until all tasks are done
