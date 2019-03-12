#!/usr/bin/python3
# A strong password is defined as one that is:
#   * at least eight characters long,
#   * contains both uppercase and lowercase characters
#   * and has at least one digit.


import re, pyperclip


lowerRegex = re.compile(r'^[^A-Z]*$')
upperRegex = re.compile(r'^[^a-z]*$')
nodigitRegex = re.compile(r'^[^0-9]*$')


def check(pword):
    result = []
    if len(pword) <= 8:
        result.append("Length smaller than 8")
    if lowerRegex.match(pword):
        result.append("Doesn't have UPPERCASE letter")
    if upperRegex.match(pword):
        result.append("Doesn't have lowercase letter")
    if nodigitRegex.match(pword):
        result.append("Doesn't have digit")
    return "\n".join(result) if len(result) > 0 else str("Passed test")


def main():
    pword = pyperclip.paste()
    print("Password: ", pword)
    print(check(pword))


if __name__ == '__main__':
    main()