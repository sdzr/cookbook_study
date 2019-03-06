#一个包含N个元素的元组或者序列，如何将他分解为N个的单独的变量

#example 1
data=['acme',12,53.1,(2012,4,5)]
print(data)
name,height,weight,date=data
print(name,height,weight,date)

#example 2
s='hello'
a,b,c,d,e=s
print(a)
#只要是可迭代的对象，都可以执行分解操作


#exmaple 3
#在做分解操作时，对于一些想丢弃的值，可以用一些用不到的变量名
_,name,height,_=data
print(name,height)