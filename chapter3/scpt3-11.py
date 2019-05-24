# 从序列中随机出元素

import random
values = [1,2,3,4,5,6]
print(random.choice(values))

# 取出N个元素
print(random.sample(values,2))

# 打乱元素的顺序,原地打乱
random.shuffle(values)
print(values)

# 产生随机数
print(random.randint(0,10))

# 产生0到1之间的浮点数
print(random.random())

# 产生N个随机byte位表示的整数
print(random.getrandbits(200))

# random模块采用的是确定性算法，即伪随机算法，梅森旋转
# 对于相同的初始序列，产生的随机状态几乎相同，不能用于蒙特卡洛模拟，产生的随机数与seed相关
random.seed(0)
print(random.getrandbits(3))
print(random.getrandbits(3))
random.seed(0)
print(random.getrandbits(3))
print(random.getrandbits(3))

# 如果要产生加密安全的随机字节序列
# 使用ssl.RANDOM_bytes()