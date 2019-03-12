#!/usr/bin/python3
# Regex search in file "*.txt" for regular expression

import os, re, glob

targetDir = "/tmp/python"
targetRegex = re.compile(r'thuan')
fileType = "*.txt"

#suppose search only in current directory
os.chdir(targetDir)
for file in glob.glob(fileType, recursive=False):
    with open(file, "r") as fr:
        for line in fr:
            if targetRegex.search(line):
                print(file + ":" + line, end="")