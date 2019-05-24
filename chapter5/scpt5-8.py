# 对固定大小的文件进行迭代

from functools import partial

RECORD_SIZE = 32
with open('data.bin','rb') as f:
    records = iter(partial(f.read,RECORD_SIZE),b'')
    for i in records:
        print(i)