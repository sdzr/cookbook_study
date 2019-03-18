#让字典保持有序
#collections 的OrderDict,这是一个双向链表，比普通的dict多耗费2倍以上的内存
#按照元素加入的顺序存储

from collections import OrderedDict

d=OrderedDict()
d['a']=[1]
d['b']=3
d['a'].append(4)
print(d)