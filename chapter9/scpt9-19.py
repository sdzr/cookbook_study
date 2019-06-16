# 在定义的时候初始化部分类成员，而不是在创建实例的时候
# 用元类，它是在定义类的时候触发
# 元类对于每个定义的类只会运行一次，在生成每个类的时候触发

import operator

# 元类，在生成其他类的时候会调用，比如StructTuple在定义的时候就会运行一次，而不是实例化的时候。
class StructTupleMeta(type):
    def __init__(cls,*args,**kwargs):
        print('meta')
        super().__init__(*args,**kwargs)
        for n,name in enumerate(cls._fields):
            setattr(cls,name,property(operator.itemgetter(n)))

# 用于其他类从它继承的基类
class StructTuple(tuple,metaclass=StructTupleMeta):
    _fields=[]
    def __new__(cls,*args):
        print('struct')
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls,args)
    def add(self,x,y):
        return x+y

class Stock(StructTuple):
    _fields=['name','shares','price']

s=Stock('amce',50,91.1)
