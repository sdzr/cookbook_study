# 创建数据处理的通道，一个完美的生成器使用方式，流处理

import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepath, top):
    for path,dirlist,filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepath):
            yield os.path.join(path,name)


def gen_opener(filenames):
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename,'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename,'rt')
        else:
            f = open(filename,'rt')
        yield f
        f.close()

def gen_concanate(iterators):
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(lines):
            yield line

lognames = gen_find('access-log*','www')
files = gen_opener(lognames)
lines = gen_concanate(files)
pylines = gen_grep('(?i)python',lines)
for line in pylines:
    print(line)