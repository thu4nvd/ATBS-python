#!/usr/bin/python3

# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os, sys
from zipfile import ZipFile

workingDir = '/tmp/python/toZip'

def main(workingDir ):
    folder = os.path.abspath(workingDir )
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
        for dirname, _, basename in os.walk(workingDir ):
            print('Adding files in %s... ' % dirname)
            # Add the current folder to the ZIP file.
            backupZip.write(dirname)
            # Add all files in that folder to the ZIP file.
            for file in basename:
                if file.startswith(os.path.basename(workingDir ) + '_') and file.endswith('.zip'):
                    continue # don't backup the backup ZIP file
                backupZip.write(os.path.join(dirname, file))
        print('Done.')
        backupZip.close()

if __name__ == '__main__':
    main(workingDir )
