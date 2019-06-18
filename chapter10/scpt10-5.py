# 将不同目录下的代码在统一的命名空间下导入
# 可以看到blak.py和grok.py在不同的包下面，但父目录相同
# 而且在两个不同目录下没有__init__.py文件，命名空间包特性会自耦给你创建一个命名空间
# 这种类型的包都可以看到spam.__file__ 看到：<module 'spam' (namespace)>

# 以spam为公共命名空间
import sys
import os
sys.path.extend([os.path.join(os.path.curdir,'foo-package'),os.path.join(os.path.curdir,'bar-package')])
import spam.blah
import spam.grok

spam.grok.F()

# 可以看到，不同包下面的模块被合并到了一个命名空间包下面spam