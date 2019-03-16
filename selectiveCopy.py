#!/usr/bin/python3

# walks through a folder tree and searches for files with .py file extension. Archive these files in to a ZIP file

import os, sys, shutil
from zipfile import ZipFile


target_dir = "/tmp"

def main(target_dir):
    zip_file = os.path.join(target_dir, 'python_scripts.zip')
    extension = '.py'
    backup(target_dir, zip_file, extension)
    print('Destination ZIP file: %s' % zip_file)


def backup(dir, zip_file, extension):
    with ZipFile(zip_file, 'w') as zfile:
        for dirname, _, files in os.walk(dir):
            ext_files = [file for file in files if file.endswith(extension)]
            if len(ext_files) > 0:
                for file in ext_files:
                    zfile.write(os.path.join(dirname, file))


if __name__ == '__main__':
    main(target_dir)
