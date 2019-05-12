# 对二进制文件的内存映射
# 即将二进制文件映射到可变字节数组中，可以随机访问其内容，或者实现就地修改
# 并不会将整个文件读取到内存，而是维持一段虚拟内存，非常之优雅

import os
import mmap


def memory_map(filename,access=mmap.ACCESS_WRITE):
    size  = os.path.getsize(filename)
    fd = os.open(filename,os.O_RDWR)
    return mmap.mmap(fd,size,access=access)

m = memory_map('tmp')
print(m[0:11])
m[0:11]= b'ZZZZZ oooo0'
m.close()

with open('tmp','rt') as f:
    print(f.read())
