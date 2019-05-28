# 编写可接受任意参数的函数
# 参数分为位置参数和关键字参数

def Foo(first,*rest):
    return (first+sum(rest))/(1+len(rest))
# rest是一个元组，属于位置参数
print(Foo(1,2,3,4,5))
s = (8,8,8)
print(Foo(1,*s))

# 关键字参数**dic，dic是一个字典
def antargs(*args,**kwargs):
    for k,v in kwargs.items():
        print(k,v)
    for v in args:
        print(v)
    print(type(args),type(kwargs))

antargs(3,4,s1='val1',s2='val2')

d = {'s1':'val1','s2':'val2'}

antargs(5,6,**d)

# *打头的参数只能作为最后一个位置参数，**打头的参数只能作为最后一个参数出现
# 在*打头的参数后面出现的参数，称之为keword-only参数，只能作为位置参数
def b(*x,y,**kwargs):
    pass
# 例如y就是一个keyword-only 参数

