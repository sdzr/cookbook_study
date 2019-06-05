# 一种新形式的类属性或者实例属性

class Integer:
    def __init__(self,name):
        self.name =name

    def __get__(self, instance, owner):
        if instance is None:
            print('insrtacne')
            return self
        else:
            print(instance.__dict__)
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(instance,value)
        if not isinstance(value,int):
            raise TypeError('Expected')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Point:
    x = Integer('X')
    y = Integer('Y')
    def __init__(self,x,y):
        self.x =x
        self.y=y

p = Point(3,4)
print(p.x)