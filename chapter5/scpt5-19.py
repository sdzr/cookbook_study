# 创建临时文件和目录

# 临时文件，关闭即自动销毁

from tempfile import TemporaryFile
from tempfile import NamedTemporaryFile

with TemporaryFile('w+t') as f:
    f.write('Hello World\n')
    f.write('Testing\n')
    f.seek(0)
    print(f.read())
# 这时文件自动销毁了

# 命名的临时文件
# delete 参数可以控制文件关闭后不自动删除
import os
with NamedTemporaryFile('w+t',prefix='mytemp',suffix='.txt',dir=os.path.curdir,delete=False) as f:
    print('filename = ',f.name)

# 临时目录
from tempfile import TemporaryDirectory
with  TemporaryDirectory() as dirname:
    print('文件名是：',dirname)
# 临时目录自动销毁