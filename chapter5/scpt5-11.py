# 处理路径名
import os
path = '/users/beazley/Data/data/data.csv'

print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.splitext(path))

# 扩充到用户目录
path = '~/data/data.csv'
print(os.path.expanduser(path))