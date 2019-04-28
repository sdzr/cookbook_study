from decimal import Decimal
# python默认的浮点数，精确到17位（包括小数点）
a = 4.2
b = 2.1
print(a+b)
print((a+b)==6.3)

# 要想做精确的计算，可以用decimal类来实现

a = Decimal('4.2')
b = Decimal('2.1')
print((a+b),(a+b)==Decimal('6.3'))

# 一般用法，通过设置上下文变量，来修改相关计算上下文环境
from decimal import localcontext

a = Decimal('1.3')
b = Decimal('1.7')

print(a/b)

with localcontext() as ctx:
    ctx.prec=3
    print(a/b)

# example 1,发现误差
a = [1e20, 1, -1e20]
print(sum(a))
from math import fsum
print(fsum(a))
