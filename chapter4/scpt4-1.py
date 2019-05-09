# 手动访问迭代器中的元素

with open('text.txt','r') as f:
    try:
        while True:
            line= next(f)
            print(line)
    except StopIteration:
        pass

# 或者让next返回Nne（结束时）
with open('text.txt','r') as f:
    while True:
        line = next(f,None)
        if line is None:
            break
        print(line)

a = [1,2,3,4]
it = iter(a)
print(next(it))
print(next(it))

