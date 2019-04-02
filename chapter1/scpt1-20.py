#将多个字典合并，

#方式一：使用ChainMap类来生成原始数据的映射，对ChainMap对象的修改会反应到原始字典上
a={'x':1,'y':2}
b={'x':3,'z':4}
from collections import ChainMap
C=ChainMap(a,b)
for k,val in C.items():
    print(k,val)

print(C['x'])  #始终只会返回第一个字典的值，在key重复的情况下,修改的时候也会这样

#方式2：用update函数更新到一起
a.update(b)  #修改b不会影响到a，相当于生成了一个新的字典。

for k,v in a.items():
    print(k,v)

