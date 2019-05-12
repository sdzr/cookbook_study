# 为已经打开的文件添加或者修改编码方式
import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u,encoding='utf8')
text =f.read()

# 对已经以文本模式打开的文件，修改编码前，首先得移除之前的编码层

import sys
print(sys.stdout.encoding)
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='latin-1')
print(sys.stdout.encoding)


# 一个文件的打开分为三层，原始文件（代表着操作系统底层的文件描述符）；IO缓冲层（负责处理二进制数据）；文本处理层（负责编码解码）


