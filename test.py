#!/usr/bin/python3
# use for testing

import re

testRegex = re.compile(r'\bhttp[s]?://\w+[.]\S+\b')
texts = [
    "http://vnexpress.nett",
    "thuan https://vietcombank.vn",
    "http://lemonde.fr/7jours cai gi do",
    "https://vietname.edu.vn"
]
for text in texts:
    print(testRegex.search(text))