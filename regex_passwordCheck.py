#!/usr/bin/python3
# A strong password is defined as one that is:
#   * at least eight characters long,
#   * contains both uppercase and lowercase characters
#   * and has at least one digit.


import re, pyperclip

def check(pword):
    criteria = [0] * 4
    if len(pword) >= 8:
        criteria[0] = 1
    return criteria

def main():
    pwRegex = re.compile(r'''
    \b
    ''')
    pword = pyperclip.paste()
    print(check(pword))


if __name__ == '__main__':
    main()