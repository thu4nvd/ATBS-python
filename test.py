#!/usr/bin/python3

import re

text = 'eWfd geef      f4f de'
chars = 'edfW'


strp_regex = re.compile(r'''
        ^
        (?:[%s])*(.*?)(?:[%s])*
        $
    ''', re.VERBOSE)


def customStrip(text, chars):
    
    result = mo.sub(r'\1', text)
    return result

print(customStrip(text, chars))