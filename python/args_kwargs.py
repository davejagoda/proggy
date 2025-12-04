#!/usr/bin/env python3


def function(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


if "__main__" == __name__:
    function("pos1", "pos2", "pos3", key1="value1", key2="value2", key3="value3")
    pos = ("a", "b", "c")
    key = {"a": 1, "b": 2, "c": 3}
    function(*pos, **key)
