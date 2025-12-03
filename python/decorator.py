#!/usr/bin/env python3

import time


def timer_decorator(base_function):
    def decorated_function(*args, **kwargs):
        a_time = time.time()
        result = base_function(*args, **kwargs)
        z_time = time.time()
        print(f"Elapsed time: {z_time - a_time:.6f} seconds")
        return result

    return decorated_function


@timer_decorator
def fib_wrapper(n):
    return fib(n)


def fib(n):
    assert n >= 0
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


d = {}


@timer_decorator
def fib_memo_wrapper(n):
    return fib_memo(n)


def fib_memo(n):
    assert n >= 0
    if n in d:
        return d.get(n)
    if n < 2:
        d[n] = n
        return n
    d[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return d[n]


for i in range(40):
    print(f"fibonacci: {i}")
    print(fib_wrapper(i))
    print(fib_memo_wrapper(i))
