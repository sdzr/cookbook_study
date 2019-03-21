#通过公共健对字典列表进行排序
rows=[
    {'fname':1,'lname':4},
    {'fname':3,'lname':2}
]

#排序时，对于sort等函数，一般都会有一个key参数，通过lambda函数可以按指定值排序
#但是，operato模块的itemgetter函数替换lambda函数，速度会更快。
from operator import itemgetter

sort_by_fname=sorted(rows,key=itemgetter('fname'))
sort_by_lname=sorted(rows,key=itemgetter('lname'))

print(sort_by_fname)
print(sort_by_lname)


sort_by_fname=sorted(rows,key=lambda x:x['fname'])
sort_by_lname=sorted(rows,key=lambda x:x['lname'])

print(sort_by_fname)
print(sort_by_lname)