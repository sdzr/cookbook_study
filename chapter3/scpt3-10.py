# 矩阵和线性代数计算

import numpy as np
mat = np.matrix([[1,2,3],[3,4,10],[4,5,6]])
print(mat)
print(mat.T)
print(mat.I)

# 一些常见的线性算法可在numpy算法库中找到
import numpy.linalg
print(np.linalg.info)