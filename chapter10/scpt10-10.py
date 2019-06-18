# 使用字符串中给定的名称来导入模块
import importlib
s='math'
m=importlib.import_module(s)

print(m.sin(2))

# 也可以相对导入加一个参数：指定包名

