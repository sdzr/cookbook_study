# 用生成器创建迭代模式
def frange(start, end, increment):
    x =start
    print('begin')
    while x <= end:
        yield x
        x += increment
    print('completed!!')

a = frange(1,100,2)
for i in a:
    print(i)