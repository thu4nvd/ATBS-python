#!/usr/bin/python3

import shelve, sys, re

with shelve.open('madLibs_file') as my_file:
    for word in ['ADJECTIVE', 'NOUN', 'VERB']:
        my_file[word] = input('Enter an %s: ' % word)

    with open('madLibs.txt', 'r') as file, open('madLibs.output', 'w') as fo:
        for line in file:
            for word in re.split(r'(\.|,|;|:|\s)\s*', line):
                if word in list(my_file.keys()):
                    fo.write(my_file[word])
                    print(my_file[word], end="")
                else:
                    fo.write(word)
                    print(word, end="")
            fo.write("\n")