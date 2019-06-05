# 将元数据信息附加到函数参数上
# 将参数上附加一些额外信息，使得其他人对函数的使用有更多的认识
# 函数的参数注解可以提示程序员该函数如何使用

def add(x:int,y:int)->int:
    return  x+y

print(add(10,5))
help(add)