# 将字符串转换为日期

from datetime import datetime

text = '2019-04-26'
print(text)
y = datetime.strptime(text, '%Y-%m-%d')
print(type(y))

# 而strftime可以将标准日期转换为其他格式
z = datetime.now()
print(z)
nice_z = datetime.strftime(z,'%A %B %d ,%Y')
print(nice_z)