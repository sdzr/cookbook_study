#从字典中提取子集，这是一个简单的问题
price={
    'a':1,
    'b':2,
    'c':3
}
p1={key:value for key,value in price.items() if value>2}

print(p1)

te={'a'}
print(te)

p2={key:value for key,value in price.items() if key in te}

print(p2)