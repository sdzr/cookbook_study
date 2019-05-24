# 将已有的文件描述符包装为文件对象

# 文件描述符：它是一个整数，由操作系统分配的，用来指代某种系统I/O通道。
# 可以对其进行包装，成为一个文件对象

import os

# 文件描述符fd
fd = os.open('tmp',os.O_WRONLY|os.O_CREAT)

f = open(fd,'wt')
f.write('hello world\n')
f.close()