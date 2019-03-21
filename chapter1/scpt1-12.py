#这是一个非常有用的函数
#找出序列中出现次数最多的函数。
from collections import Counter

a=['1','a','a','b','b','b']

wordcount=Counter(a)
#事实上wordcount 是一个字典，可以当作字典来操作
print(wordcount.most_common(2))

wordcount['a']=wordcount['a']+2

print(wordcount['a'])

#而且wordcount对象可以做加减操作，对应的计数（value）会被加上。

#可以在一个wordcount上面继续count更多的序列
b=['d','d']
wordcount.update(b)
print(wordcount)