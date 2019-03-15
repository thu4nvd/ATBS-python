#!/usr/bin/python3

import os, re, shutil
import logging

target_dir = '/tmp/python'
seq = re.compile(r'^(spam)(\d+)(.txt)')
logging.basicConfig(filename='fillingGaps.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

lst = []
for file in os.listdir(target_dir):
    num = seq.search(file).group(2)
    lst.append( (int(num.lstrip('0')), file, len(num)) )

lst = sorted(lst)
logging.debug(lst)

for index in range(len(lst)):
    padding = lst[index][2]
    num = str(int(index) + 1)
    padded_num = num.rjust(padding, '0')
    src = os.path.join(target_dir, lst[index][1])
    dst = os.path.join(target_dir, seq.sub(r'\g<1>%s\g<3>' % padded_num, lst[index][1]))
    shutil.move(src, dst)

# for i in 001 002 004 005 006 009 ; do touch spam$i.txt ; echo spam$i >> spam$i.txt ; done    
# for i in 001 002 004 005 006 009 ; do touch ${dir}/spam$i.txt ; echo $i > ${dir}/spam$i.txt ; done
# for i in 011 012 014 025 026 319 ; do touch ${dir}/spam$i.txt ; echo $i > ${dir}/spam$i.txt ; done
