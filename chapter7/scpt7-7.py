# 在匿名函数中绑定变量的值

# 运行时绑定,而非定义时绑定
x =10
a = lambda y:x+y
x = 20
b = lambda y:x+y
print(a(10),b(10))

# 若要改成定义时绑定
a = lambda y,x=x:x+y

# 看个典型的例子
funs = [lambda x:x+n for n in range(5)]
for f in funs:
    print(f(0))

funs = [lambda x,n=n:n+x for n in range(5)]

for f in funs:
    print(f(0))