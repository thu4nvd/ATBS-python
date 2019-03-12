#!/usr/bin/python3

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - delete keywords from clipboard.

import pyperclip, shelve, sys, pprint

with shelve.open('mcb') as mcbShelf:
    if len(sys.argv) == 3:
        key = sys.argv[2]
        # Save clipboard content.
        if sys.argv[1].lower() == 'save':
            # don't use "all" key cause it has spec meaning
            if key.lower() == 'all':
                print("'all' has special meaning. Don't use it as keyword.")
                sys.exit()
            else:
                clipBoard = pyperclip.paste()
                mcbShelf[key] = clipBoard
        # Delete clipboard content.
        elif sys.argv[1].lower() == 'delete':
            # delete all keyvalues
            if key.lower() == 'all':
                for key in list(mcbShelf.keys()):
                    del mcbShelf[key]
            # delete specific keyvalue
            elif key.lower() in list(mcbShelf.keys()):
                del mcbShelf[key]
            else:
                print('There is not such a keyvalue %s' % key)
    elif len(sys.argv) == 2:
      # Loads all keywords to clipboard
      if sys.argv[1].lower() == 'list':
        keys = list(mcbShelf.keys())
        pprint.pprint(keys)
      # List keywords and load content.
      elif sys.argv[1].lower() in mcbShelf:
        key = sys.argv[1]
        pyperclip.copy(mcbShelf[key])
mcbShelf.close()

# Project
# Extending the Multiclipboard

# Mad libs
# Create a Mad Libs program that reads in text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For
# example, a text file may look like this:
# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
# unaffected by these events.
# The program would find these occurrences and prompt the user to replace them.
# Enter an adjective:
# silly
# Enter a noun:
# chandelier
# Enter a verb:
# screamed
# Enter a noun:
# pickup truck
# The following text file would then be created:
# The silly panda walked to the chandelier and then screamed. A nearby pickup
# truck was unaffected by these events.
# The results should be printed to the screen and saved to a new text file.

# Regex Search
# Write a program that opens all .txt files in a folder and searches for any line that matches a
# user-supplied regular expression. The results should be printed to the screen.