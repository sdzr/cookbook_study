# 发布自定义的包，可以用python setup.py install
# 安装到python，可以import导入的哟

#创建两个文件
#setup.py
from distutils.core import setup

setup(name='projectname',version='1.0',
      author='leishenghua',
      author_email='290701331@qq.com',
      url='http://www.leishenghua.com.projectname',
      packages=['projectname','projectname.utils'])



# MANIFEST.in
# include *.txt
# recursive-include examples *
# recursive-include Doc *



#bash python3 seetup.py sdist