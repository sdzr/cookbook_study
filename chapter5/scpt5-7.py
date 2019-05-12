# 读取以gzip和bz2格式压缩过的文件

import gzip
import bz2
with gzip.open('tmp.gz','wt') as f:
    f.write('hello world')

with gzip.open('tmp.gz','rt') as f:
    data = f.read()


# 可以对已经打开的二进制文件进行叠加操作
f = open('tmp.gz','rb')
with gzip.open(f,'rt') as g:
    text = g.read()
print(text)
