# 拷贝或者移动文件和目录，但是不想通过调用shell来完成

import shutil

# cp src dst
shutil.copy(src,dst)

# cp -p src dst,包含元数据
shutil.copy2(src,dst)

# cp -R src dst
shutil.copytree(src,dst)

# move src dst
shutil.move(src,dst)

# 忽略某些文件，不拷贝
shutil.copytree(src,dst,ignore=shutil.ignore_patterns('*~','*.pyc'))

