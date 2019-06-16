# 以简单的方式定义上下文管理器
#

import time
from contextlib import contextmanager

@contextmanager
def list_transaction(origin_list):
    working=origin_list
    # yield 之前相当于__enter__方法
    yield working
    # yield之后相当于__exit__方法
    origin_list[:]=working

items = [1,2,3,4]
with list_transaction(items) as working:
    working.append(5)
    working.append(6)
print(items)