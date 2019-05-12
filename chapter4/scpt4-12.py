# 在不同容器中迭代
from itertools import chain

xpts = [1,3,4,5]
ypts = ['a','b','c']

s = chain(xpts,ypts)

for i in s:
    print(i)