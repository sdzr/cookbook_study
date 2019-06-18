# c重新加载模块，不太安全
# 当修改了一个已经加载的模块后，得重新加载一下
import os
import imp
imp.reload(os)
# 只会更新import 导入的，而不会更新from XXX import AA 的模块