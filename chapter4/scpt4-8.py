# 跳过可迭代对象的前一部分
# 注意，此处只丢弃了前一部分

from itertools import dropwhile
import os
path = r'scpt4-7.py'
path = os.path.join(os.path.curdir,path)
with open(path, 'r',encoding='utf8') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end=' ')
