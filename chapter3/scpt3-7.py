# 无穷大和NaN

a = float('-inf')
b = float('inf')
c = float('NaN')
print(a, b, c)

print(a+10)
print(c+10)

import math
print(math.isinf(b))
print(math.isinf(c))