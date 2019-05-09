# 好玩
# 将一列元素按所有可能的组合进行排列和组合


#全排列
from itertools import permutations

items = ['a', 'b', 'c']
for i in permutations(items):
    print(i)

# 而且长度可选
for p in permutations(items,2):
    print(p)

#全组合
from itertools import combinations,combinations_with_replacement

for p in combinations(items,3):
    print(p)

for p in combinations(items, 2):
    print(p)

# 以上是将选择过的元素排除了，即‘a’只会出现一次，在一个组合中。
for p in combinations_with_replacement(items,3):
    print(p)