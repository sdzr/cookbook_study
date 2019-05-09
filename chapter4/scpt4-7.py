#  对迭代器做切片操作
# 普通的切片方法会报错
from itertools import islice


def count(n):
    while True:
        yield n
        n += 1

f = count(1)

for i in islice(f, 10, 20):
    print(i)
