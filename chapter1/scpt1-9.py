#在两个字典中寻找相同点，相同的key或者value
#字典的key是可以做集合的所有操作的，因为key具有唯一性，而值则不可以。
a={
    'x':1,
    'y':2,
    'z':3
}

b={
    'w':10,
    'x':1,
    'y':2
}
print(a.keys()&b.keys())
print(a.keys()-b.keys())
print(a.items()&b.items())
print({key:a[key] for key in a.keys()-{'z','w'}})
print(a.keys())