# 数据汇总和统计
# 使用pandas库就行了


import pandas as pd

data =pd.read_csv('stocks.csv')

print(data)

print(data['Symbol'].unique())
