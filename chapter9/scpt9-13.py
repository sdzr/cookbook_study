#  通过元类来开控制实例的创建
#  元类就是可以创建类的类，比如type，他返回的对象是类，而不是类实例对象，元类就是创建类这种对象的东西
#  Python中所有的东西，注意，我是指所有的东西——都是对象。这包括整数、字符串、函数以及类。它们全部都是对象，而且它们都是从一个类创建而来
# 定义一个元类，重新实现它的__call__（）方法

class Singleton(type):
    def __init__(self,*args,**kwargs):
        self.__instance=None
        super().__init__(*args,**kwargs)

    def __call__(self,*args,**kwargs):
        if self.__instance is None:
            self.__instance=super().__call__(*args,**kwargs)
            return self.__instance
        return self.__instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')

a=Spam()
b=Spam()
print(a is b)
c = Spam()
print(a is c)
