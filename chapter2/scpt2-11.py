# 从字符中去除不需要的字符
# 以空格为例
a = ' hello      world \n'
print(a.strip())
print(a.lstrip())
print(a.rsplit())

# 如果要去掉中间的某些字符
# 可以使用replace函数或者用正则化re.sub替换掉

print(a.replace(' ', ''))
import re
print(re.sub(r'\s+', '', a))
