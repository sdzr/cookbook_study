#  避免出现重复的属性方法

# 在初始化的时候会被调用，所以要用到self
def type_property(name,expected_type):
    storage_name='_'+name
    @property
    def prop(self):
        print('ok')
        return getattr(self,storage_name)

    @prop.setter
    def prop(self,value):
        print('ok1')
        if not isinstance(value,expected_type):
            raise TypeError('{} must be a {}'.format(name,expected_type))
        setattr(self,storage_name,value)
    return prop

class Person:
    name=type_property('name',str)
    age=type_property('age',int)
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=Person('A',10)
print(p.name)