import sys
import os
path= os.path.dirname(__file__)
print(path)
sys.path.insert(0,'sss')
print(sys.path)

# 方法2
# 也可通过在site-package 目录夹下创建一个,pth文件1
# myapplication.pth
# /some/dir
# 这样/some/dir就会在解释器启动的时候自动加入到sys.path中