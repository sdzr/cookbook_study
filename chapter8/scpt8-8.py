# 崽子类中扩扩展属性

class Person:
    def __init__(self,name):
        self.name=name
    # getter function
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError('Excected a string')
        self._name=value


# 在子类中扩展其中属性
class SubPerson(Person):
    @property
    def name(self):
        print('Geting name')
        return super().name

    @name.setter
    def name(self,value):
        print('set name',value)
        super(SubPerson,SubPerson).name.__set__(self,value)

# 如果只是想扩展属性中的一个方法
class sPerson(Person):
    @Person.name.setter
    def name(self,value):
        print('set a name',value)
        super(sPerson,sPerson).name.__set__(self,value)