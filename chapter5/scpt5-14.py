# 绕过默认的文件名编码，即不安文件名的编码方式，来给内容解码，存在一些恶意修改问题，要绕过默认编码
# 如果要绕过，可以使用原始的字符串来指定文件名
import sys
print(sys.getfilesystemencoding())


# 不常用