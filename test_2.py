#!/usr/bin/python

import shelve

with shelve.open("test") as outShelve:
    print(outShelve['a'])
    print(outShelve['b'])