# 基于REST风格的简单接口

import cgi

a = {}
a['a','b']=10
print(a)
print(a.get(('a','b'),lambda:print('ok')))