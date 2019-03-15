#!/usr/bin/python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
# Usage: 
#   1. Copy the target text to clipboard
#   2. Run this script: python3 bulletPointAdder.py
#   3. Paste the result text

import pyperclip

def main():
    text = pyperclip.paste().split('\n')

    mod_text = ''
    for line in text:
        mod_text += '* ' + line + '\n'

    pyperclip.copy(mod_text)

if __name__ == "__main__":
    main()
    
# WhatNext
# Apply to whatever modification of clipboard's content
# Filter: filter for phone, url, object, etc..
# Format: clean up data
# Populate: generate whatis information of command
        # Refer database and retrieve infomation
# Transform: translate to other language
    # accenter or unaccenter vietnamese