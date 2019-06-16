# 把装饰器加到类方法和静态方法上
# @staticmethod,@classmethod 返回的是修饰符，而不是可调用的对象
# 所以一般以上两个装饰器必须在最外围
import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        r=func(*args,**kwargs)
        end=time.time()
        print(end-start)
        return r
    return wrapper

class Spam:
    @timethis
    def instance_method(self,n):
        print(self,n)
        while n>0:
            n-=1

    @classmethod
    @timethis
    def class_method(cls,n):
        print(cls,n)
        while n>0:
            n-=1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n>0:
            n-=1

s =Spam()
s.instance_method(100)
Spam.class_method(100)
Spam.static_method(100)
