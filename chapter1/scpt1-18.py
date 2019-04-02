#将名称映射到列表的元素当中
from collections import namedtuple
#namedtuple 是一个工厂函数，因此返回的是一个标准元组类型的子类
SubScriber=namedtuple('subscb',['addr','phone','age']) #这是一个类，元组名为subscb，元组元素名
sub=SubScriber('here','18811145369',None)

print(sub)
print(sub.addr,sub.age)

#对于普通的元组，是不可更改的，但是namedtuple可以通过——__replace()函数更改
def dict_to_tuple(s):
    #print(**s)
    return sub._replace(**s)
a={'addr':'here','phone':'18811145369'}
print(dict_to_tuple(a))

b={'addr':'here','phone':'18811145369','age':18}
print(dict_to_tuple(b))
b