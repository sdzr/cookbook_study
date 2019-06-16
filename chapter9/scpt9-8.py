# 在类中定义装饰器

from functools import wraps

class A:
    def decorate1(self,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('Decorator 1')
            return func(*args,**kwargs)
        return wrapper
    @classmethod
    def decorate2(cls,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('decorator 2')
            return func(*args,**kwargs)
        return  wrapper
a = A()
@a.decorate1
def spam():
    pass

@A.decorate2
def spam():
    pass