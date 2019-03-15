#!/usr/bin/python3

import sys, re

# def isPhoneNumber(number):
#     num = []
#     number = number.split('-')
#     for i in range(len(number)):
#         if not number[i].isdigit():
#             sys.exit()
#         elif i < 2 and len(number[i]) == 3:
#             num.append(number[i])
#             continue
#         elif i == 2 and len(number[i]) == 4:
#             num.append(number[i])
#             continue
#         else:
#             sys.exit()
#     return '-'.join(num)

# #print(isPhoneNumber(number))

phone_number = '311-335-4433'
str_number = 'fsfddsf 311-335-4433 fwfgeg 311-335-44354'

phoneRegex = re.compile(r'\s\d{3}-\d{3}-\d{4}\s')
#print pattern
results = re.findall(phoneRegex, str_number)
for result in results:
    print(result.strip())
