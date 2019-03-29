#筛选序列中的元素
from itertools import  compress  #接受一个可迭代对象和一个布尔型列表，返回一个根据bool列表筛选出迭代对象元素的迭代器

#列表推导式过滤法
mylist=[1,2,3,4,6,-4,7,-3,-1,6,9,12]
re=[n for n in mylist if n>0]   #返回的是一个列表

#生成器表达式，返回的是一个迭代器
re1=(n for n in mylist if n>0)

#filter 函数加 自定义函数 过滤法,返回一个迭代器
def fun(val):
    if val>0:
        return True
    else:
        return  False

re3=filter(fun,mylist)

#compress 过滤方法,返回一个迭代器,优点，可以通过一个列表去筛选另一个列表
bool_list=[n>0 for n in mylist]
re4=compress(mylist,bool_list)

print(re1,re,re3,re4)