# 处理大型数组的计算
# numpy的主要特点是为python提供了数组对象，而且比list性能更好

import numpy as np

# 注意list与arr的不同
a = [1, 2, 3, 4, 5]
print(a*2)
print(a+a)
b = [1, 6, 7, 8, 9]
arr = np.array(a)
print(arr+10)
print(arr.fill(11))
print(np.sqrt(arr))

c = np.array([[1,13,4],[11,4,22]])
d = np.where(c<10,c ,100)
print(c)
print(d)