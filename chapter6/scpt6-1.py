# 读写csv数据

import csv

# 每一行是元组
with open('stocks.csv') as f:
    f_csv=csv.reader(f)
    headers=next(f_csv)
    print(headers)
    for row in f_csv:
        print(row)

# 考虑到索引常常会混淆
from collections import namedtuple

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    ROW = namedtuple('ROW',headers)
    for r in f_csv:
        # 每次放入一行元素
        # *r相当于放了一行参数
        row=ROW(*r)
        print(row.Symbol)

# 将数据读取为字典
# 每一行是一个字典
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)
        print(row['Symbol'])


# 写入csv,数据是元组的时候
headers =  ['A','B','C']
rows = [(1,2,4),(5,6,7)]
with open('tmp.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

# 当数据是字典的时候
headers = ['A','B','C']
rows =[{'A':1,'B':2,'C':3},{'A':5,'B':6,'C':7}]
with open('tmp.csv','w') as  f:
    f_csv=csv.DictWriter(f,headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
