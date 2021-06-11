#!/usr/bin/python3

import re

text = 'eWfdgeeff4fde'
chars = 'edfW'


def customStrip(text, chars):
    mo = re.compile(r'''
        ^
        (?:[%s])*(.*?)(?:[%s])*
        $
    ''' % (chars, chars), re.VERBOSE)
    result = mo.sub(r'\1', text)
    return result

print(customStrip(text, chars))