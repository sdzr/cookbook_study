# 定义带有默认参数的函数

def pam(a,b=42):
    print(a,b)

# 如果默认参数是元组，字典等，默认参数应该用None

def pam(a,b = None):
    print(a,b)


# 默认参数总是在函数定义的时候就被绑定了
x = 42

def pam(a,b =x):
    print(a,b)

pam(1)
x=10
pam(3)
# 可以看到，默认参数并不会被改变
