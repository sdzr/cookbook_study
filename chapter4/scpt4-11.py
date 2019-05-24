from itertools import zip_longest
# 同时迭代多个序列
xpts = [1, 3, 4, 5, 7]
ypts = [2, 4, 6]

for x,y in zip(xpts,ypts):
    print(x,y)


for x,y in zip_longest(xpts,ypts):
    print(x,y)
