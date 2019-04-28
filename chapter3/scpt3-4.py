#  进制转换
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

#  如果不想带上前缀
print(format(x,'b'))
print(format(x, 'o'))
print(format(x, 'x'))

# 要将其他进制数据转换为十进制

s = format(x, 'b')
s1 = format(x ,'o')
print(int(s, 2))
print(int(s1, 8))