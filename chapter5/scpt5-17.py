# 将字节数据写入文本文件
# 可以直接绕过编码层，将数据写入IO缓存层
import sys

sys.stdout.buffer.write(b'hello\n')


