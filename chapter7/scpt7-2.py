# 编写只接受关键字参数的函数
# 在*args 或者* 后面的参数，就会时key-only参数

def recev(maxsize,*,block):
    print(maxsize,block)

recev(10,block='ssss')


def minsiz(*value, clip=None):
    print(value,clip)

minsiz(1,2,3)
minsiz(1,clip='s')
a =(1,3,4,5)
minsiz(*a,clip=1000)