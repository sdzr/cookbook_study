#实现优先级的队列
#实现一个队列，按给定的优先级给队列排序
#使用到heapq模块
#主要解决的问题，对于由相同优先级的元素，在进行‘>’排序的时候，会报错
#因此，在给元素中加一个index，在优先级相同的时候，索引不一样，这时>不会报错
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue=[]
        self._index=0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index+=1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q=PriorityQueue()
q.push(Item('leishenghua'),1)
q.push(Item('user4'),2)
q.push(Item('LSH'),1)

print(Item('LSH'))
print(q.pop())
print(q.pop())
print(q.pop())
