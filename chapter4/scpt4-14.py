# 扁平化的处理嵌套型序列
# 例如将嵌套的list解析成单个的元素，忽略掉字符串
from collections import Iterable


def flatten(items, ignore_type = (str,bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x,ignore_type):
            yield from flatten(x)
        else:
            yield x

items = [1,2, [3,4, [5, 6],8],10]

for i in flatten(items):
    print(i)
