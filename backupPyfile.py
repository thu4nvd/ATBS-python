#!/usr/bin/python3

# backupPyfile.py - Copies only *.py file into
# a ZIP file whose filename increments.

import os, sys, re
from zipfile import ZipFile


working_dir = '/tmp/python/toZip'
# file_type = "*.py"
extRegex = re.compile(r'^.*\.py$')
# change regex to filter the file file_type
# only py file                    r'.*[.](py)$'
# only py and txt file            r'.*[.](py|txt)$'
# all except py and txt file      r'.*[.](?!bat$|exe$)[^.]*$'


def main(working_dir):
    folder = os.path.abspath(working_dir)
    backupToZip(folder)


def backupToZip(folder):
    number = 1
    while True:
        zipFileName = os.path.join(os.path.dirname(folder), os.path.basename(folder) + '_' + str(number) + '.zip')
        if not os.path.exists(zipFileName):
            break
        number += 1

    # Creating the ZIP file
    print('Creating %s... ' % zipFileName)
    with ZipFile(zipFileName, 'w') as backupZip:
        for dirname, _, files in os.walk(working_dir):
            for file in files:
                if extRegex.match(file):
                    backupZip.write(os.path.join(dirname, file))
        print('Done.')
        backupZip.close()

if __name__ == '__main__':
    main(working_dir)
