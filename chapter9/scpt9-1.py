# 元编程：目标就是创建类和函数。

# 装饰器的使用，添加一个包装层，以添加额外的处理（记录日志，计时统计）
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

countdown(100000000)