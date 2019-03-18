#在字典中，将健值映射到多个值上面
#为了避免麻烦的字典初始化问题，可以采用collections中的defaultdict
from collections import defaultdict
d=defaultdict(list)
d['a'].append(1)
d['a'].append(3)
d['b'].append(2)
print(d)
#以上自动的创建了字典表项，上面为每一个key创建了一个list
#如果不想要这个功能，可以如下写法
d={}
d.setdefault('a',[]).append(10)
d.setdefault('c',[]).append(4)
print(d)

