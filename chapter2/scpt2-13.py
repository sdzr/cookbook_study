# 对齐字符串文本
# 方法很多，只要掌握format函数即可
# 左对齐<,右对齐>,中间^,可以接对齐的填充字符，如=
# 方法一
s = 'hello world'
print(format(s, '=<20'))
print(format(s, '=>30'))
print(format(s, '*^40'))
x = 1.2345
print(format(x, '=>10.2f'))



# 当格式化多个值的时候，也可以用format函数
print('{:=>20} {:=>20}'.format('hello', 'world'))

# 方法2 ljust,rjust,center
print(s.ljust(20, '='))
print(s.rjust(20, '='))
print(s.center(30, '*'))

#

