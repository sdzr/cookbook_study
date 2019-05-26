# 让带有N个参数的可调用对象以较少的参数的方式调用

from functools import partial

def myfun(a,b,c,d):
    print(a,b,c,d)

s = partial(myfun,1)
s(3,4,5)


# 经典用法，对于一些参数为回调函数时，而这个回调函数需要传入参数，但是又无法传入参数
# 这时可以使用partial