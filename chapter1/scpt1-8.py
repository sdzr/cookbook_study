#与字典相关的计算问题
#利用zip函数将key与value对调过来是非常合适的,zip会产生一个迭代器，只被消费一次
prices={
    'g':1,
    'b':3,
    'c':4,
    'e':3
}
min_price=min(zip(prices.values(),prices.keys()))
print(min_price)

prices_sort=sorted(zip(prices.values(),prices.keys()))
print(prices_sort)

#如果直接在字典上做常规的数据操作，处理的会是key
print(min(prices))

#传入的是key
print(min(prices,key=lambda k:prices[k]))
