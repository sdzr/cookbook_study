# 编写装饰器的时候如何保存元数据
# 元数据：函数名，文档字符串，函数注解，以及调用签名
# 解决方案：只要调用functools.wraps就可以了，它通过__wapperd__属性来访问被包装的那个函数

import time
from functools import wraps

def timethis(func):
    '''decorator that reports the execute time'''
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__,end-start)
        return result
    return wrapper

@timethis
def countdown(n:int)->None:
    '''
    counts down
    :param n: 输入整数
    :return: 不返回
    '''
    while n>0:
        n=n-1

countdown(10000000)
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)
print(countdown.__wrapped__(1000))
