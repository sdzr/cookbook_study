# 读写文本数据

# python默认将window下的换行\r\n换成\n,加上newline='' 参数之后，可以关掉这种翻译。

import os
path = os.path.join(os.path.curdir,'scpt4-15.py')
with open(path,'r',encoding='utf8',newline='') as f:
    data = f.read()

print(repr(data))