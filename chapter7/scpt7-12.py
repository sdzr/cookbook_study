# 访问定义到比闭包的变量
def sample():
    n = 0
    def func():
        print('n=',n)

    def set_n(value):
        nonlocal n
        n=value

    def get_n():
        return n
    func.get_n=get_n
    func.set_n=set_n
    return func
f = sample()
f()
f.set_n(100)
f()