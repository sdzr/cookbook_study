#对不原生支持比较操作的对象排序，如一个自定义的数据结构
#与上一节相似，sorted，max,min函数等都有一个用来传递可调用对象（callable）的参数key，而该可调用对象返回待排序对象中的某些值
#sorted则利用这些值进行排序
# operator.attrgetter
from operator import attrgetter

class User:
    def __init__(self,uid):
        self.uid=uid
    def __repr__(self):
        return 'User({})'.format(self.uid)

users=[User(11),User(3),User(5)]
sort_by_uid=sorted(users,key=attrgetter('uid'))
print(sort_by_uid)

sort_by_uid=sorted(users,key=lambda x:x.uid)
print(sort_by_uid)

#同样，attrgetter的速度会更快，同时还支持多个字段的排序