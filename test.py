#!/usr/bin/python3
# use for testing

import os, glob

dirname = "/tmp/python"
os.chdir(dirname)
print(os.getcwd())

for file in os.listdir():
    if not os.path.isfile(file):
        print(file)