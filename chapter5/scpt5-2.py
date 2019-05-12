# 将输出重定向到文件中
# 只需要在print后面加参数即可
import os
with open('tmp','w') as f:
    print('hello world!',file=f)

