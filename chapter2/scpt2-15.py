# 给字符串中的变量名做插值处理


class Info:
    t = 1000
    def __init__(self, m, n):
        self.m = m
        self.n = n

a = Info(10, 100)

print(vars(a))

# 如果存在这个变量,那么可以变量替换
m = 10
n = 10
print(vars())

s = 'dfa\'{m}\', daf{n}'
print(s.format_map(vars()))

