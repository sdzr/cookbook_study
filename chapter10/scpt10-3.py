# 用相对名称来导入包中的子模块

# 相对导入只有在特定条件下才起作用
#  1.只能使用from . import XXX的格式，不能直接import
#  2.看起来可以通过相对导入访问整个文件系统，实际上不能跳过定义包的那个目录
#  3.位于脚本顶层目录的模块不能使用相对导入
#  4.如果包的某个部分直接以脚本的形式执行，则不能使用相对导入
#     必须加上参数 -m，告诉是运行的一个模块： python -m  mymodule.py

from . import tmp