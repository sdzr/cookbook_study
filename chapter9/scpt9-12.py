# 利用装饰器给类定义打补丁

def log_getattribute(cls):
    origin_getattribute=cls.__getattribute__

    def new_getattribute(self,name):
        print('getting',name)
        return origin_getattribute(self,name)

    cls.__getattribute__=new_getattribute
    return cls
@log_getattribute
class A:
    def __init__(self,x):
        self.x=x
    def spam(self):
        pass

a=A(3)
print(a.x)
a.spam()