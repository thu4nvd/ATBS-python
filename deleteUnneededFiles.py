#!/usr/bin/python3

import os
from send2trash import send2trash

target_dir = '/tmp'
target_size = 1024 # size in MB

multiplicator = 1000 * 1000.0
target_size = target_size * multiplicator
large_files = []

for dirname, subdir, basename in os.walk(target_dir):
    # Ignore mounted remote storage.
    if dirname.startswith('/home/user_xxx/'):
        continue
    # large_files.extend( [ (os.path.join(dirname, x), round(os.path.getsize(os.path.join(dirname, x)) / multiplicator, 6)) 
    # for x in basename if os.path.getsize(os.path.join(dirname, x)) > size ] )
    for f in basename:
        file = os.path.join(dirname, f)
        file_size = os.path.getsize(file)
        if file_size > target_size:
            large_files.extend((file, round(file_size / multiplicator, 6)))

for path, size in large_files:
    print(path, size)

#    large_files.extend( [ os.path.join(dirname, x) for x in basename if not os.path.exists(os.path.join(dirname, x)) ] )
#for path in large_files:
#    send2trash(path)

