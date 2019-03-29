#根据字段对数据进行分组
#itertools.groupby函数，在分组之前必须进行排序，否则无法得到想要的分组
#groupby 每次都会返回一个值（value）和一个子迭代器，里面是值所对应的组的内容

#对字典列表分组

from operator import itemgetter
from itertools import groupby

rows=[
    {'address':'a','date':'2017-01-01'},
    {'address':'b','date':'2018-01-01'},
    {'address':'c','date':'2017-01-01'}
]
#排序先
rows.sort(key=itemgetter('date'))

for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ',i)


#用字典以一健多值的方式存储
from collections import defaultdict
dic=defaultdict(list)

for row in rows:
    dic[row['date']].append(row)
for key,val in dic.items():
    print(key,val)

print(dic.__len__())
