#!/usr/bin/python3
def add_all(*args):
    total = 0
    for arg in args:
        total += int(arg)
    print(total)
