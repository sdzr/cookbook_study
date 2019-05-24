# 检测文件是否存在

import os

print(os.path.exists('tmp'))
print(os.path.isfile('tmp'))
print(os.path.isdir('tmp'))
print(os.path.islink('tmp'))
#print(os.path.realpath('a link'))
print(os.path.getsize('tmp'))
import time
print(time.ctime(os.path.getmtime('tmp')))
print(os.path.getctime('tmp'))
print(time.ctime(os.path.getatime('tmp')))
