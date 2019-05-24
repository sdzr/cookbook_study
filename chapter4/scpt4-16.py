# 用迭代器取代while循环

# iter函数的用法，接受一个无参数的可调用对象和一个哨兵（结束）值作为输入
# 返回一个迭代器
import os
path = os.path.join(os.path.curdir,'scpt4-11.py')

f = open(path,'r',encoding='utf8')

for line in iter(lambda:f.read(),''):
    print(line)
