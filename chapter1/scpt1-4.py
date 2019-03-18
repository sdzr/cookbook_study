#在某个集合中，找出最大或者最小的N个值
#example 1:
import heapq
nums=[1,2,3,4,5,-9,4,23]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

#example 2
#这个函数还可以指定一个key参数，因此可以这样用,按指定元素，选出最大的值
#当N的值比较小的时候，这种方式的速度会很快

portfolio=[
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'AAPLE','shares':50,'price':54.43},
    {'name':'HPQ','shares':200,'price':21.09},
]
cheap=heapq.nsmallest(2,portfolio,key=lambda s :s['price'])
expensive=heapq.nlargest(2,portfolio,key=lambda s:s['price'])

print(cheap,expensive)

#对一个队列进行堆排序，heap[0]永远是小的那个值，pop出之后会更新，操作的复杂度为O（logN）
nums=[1,7,32,-4,-18,28,37]
heap=list(nums)
heapq.heapify(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
print(type(heap))