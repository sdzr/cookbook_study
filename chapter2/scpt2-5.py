#查找和替换文本
text='Today is 11/27/2012. PyCon starts 3/13/2013'
#最简单的方法
text=text.replace('Today','test')
print(text)

#d对于复杂一点的查找替换，可以用re.sub和re.subn，二者相同，只不过subn会多返回一个替换次数
import re
pattern=r'(\d+)/(\d+)/(\d+)'
datepate=re.compile(pattern)
s=datepate.sub(r'\3-\1-\2',text)  #解释\2,\3,\1,分别代表pattern里面的三个捕获组
print(s)
s=datepate.sub(r'\3-\1-\2',text)
print(s)


#对于更加复杂的，可以写一个回调函数来替换
from calendar import month_abbr
def change_date(m):
    mon_nm=month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mon_nm,m.group(3))

s = datepate.sub(change_date, text)
print(s)

print(type(month_abbr))

#记录一个小知识,关于在模块开头定义的__all__=['a','b']变量。
#当使用 from package import *，默认只导入__all__中的类容，
#如果不定义__all__,则会导入所有非私有函数，类。
#可以以calendar源码为例。