# 对数值进行取整
a = 345.765908
print(round(a,3))
print(round(a,-1))


# 注意取整与format格式化是不同的，虽然也可以用format指定精确度

s = 'value is {:0.3f}'.format(a)

print(s)