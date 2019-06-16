#在*args和**kwargs上强制规定一种参数签名

from inspect import Signature,Parameter,signature
# 方法一
def makesig(*names):
    parms = [Parameter(name,Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)
class Structure:
    __signature__=makesig()
    def __init__(self,*args,**kwargs):
        bound_values=self.__signature__.bind(*args,**kwargs)
        for name,value in bound_values.arguments.items():
            setattr(self,name,value)
class Stock(Structure):
    __signature__ = makesig('name','shares','price')


print(signature(Stock))

# 方法二，元类的解决方法
