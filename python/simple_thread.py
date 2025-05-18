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
        print(f"{word}:{(word)}", flush=True)


def worker(num):
    while True:
        word = q.get()
        if args.verbosity > 1:
            name = threading.current_thread().name
            ident = threading.current_thread().ident
            native_id = threading.current_thread().native_id
            print(
                f"THREAD:{num} {name} {ident} {native_id} got {word}",
                flush=True,
            )
        do_work(word)
        q.task_done()


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--thread_count", type=int, default=1)
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
if args.verbosity:
    print(f"thread_count:{args.thread_count}", flush=True)

q = queue.Queue()
for i in range(args.thread_count):
    t = threading.Thread(target=lambda j=i: worker(j), name=f"Thread-{i}")
    t.daemon = True
    t.start()

for word in source():
    if args.verbosity > 1:
        print(f"raw word:{word}", flush=True)
    q.put(word)

q.join()  # block until all tasks are done
