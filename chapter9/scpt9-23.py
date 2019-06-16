# 执行带有局部副作用的代码

# 现象
def test1():
    a =13
    b=0
    exec('b =a+10')
    print(b)

test1()

# 原因：exec的传入参数，默认是局部变量和全局量的一个拷贝
# 所以当exec运行完了之后，还需要将被修改的变量传回来，才可以看到修改的地方
# locals函数，获取当前局部变量的一个拷贝

def test2():
    print()
    a =13
    loc= locals()
    print(loc)
    exec('b=a+10')
    print(loc)
    a = loc['b']
    print(a)

test2()

#也可以自定义两个字典局部变量和全局变量传入到exec里面。