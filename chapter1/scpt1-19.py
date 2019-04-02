#核心知识，即注意生成器的使用，减小不必要的list生成
a=[1,2,3,4,5,90,-45,10,9]
s=min(v for v in a if v>0)
print(s)


#可以看到
s=min((v for v in a if a>0))
print(s)

#两种方式的效果一样