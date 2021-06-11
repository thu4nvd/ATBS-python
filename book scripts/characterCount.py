from pprint import pprint, pformat

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

DICT = {}

for char in message.upper():
    DICT[char] = DICT.get(char, 0) + 1
pprint(DICT)

# wordDict = {}
# for drow in message.upper().split():
#     wordDict[drow] = wordDict.get(drow, 0) + 1
# pprint(wordDict)
# voi viec chon tu thi phai tokenize chuan xac hon