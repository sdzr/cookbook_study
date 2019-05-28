# 当创建大量实例时，如何节省内存

# 使用__slot__属性，这样就不会对每一个实例都创建一个__dict__，而是紧凑的存为数组
# 副作用是，不能再添加新的属性，只有这里面的属性
# 最好是用在简单的数据结构上，他会导致python中基于字典实现的依赖无法使用

class Date:
    __slots__ = ['year','month','day']
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

p =Date(2012,12,31)