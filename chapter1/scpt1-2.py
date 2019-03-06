#从任意长度的可迭代对象中分解元素
#从某个迭代对象中，分解出N个变量，但是迭代对象的长度可能超过N

#example 1
record=('Dave','Dave@example.com','773-555-1212','847-555-1212')
name,email,*phone_number=record
print(name)
print(phone_number)
#对于phone_number变量，不管它包含几个值，他都是一个list

#example 2
#在传参的时候可以带*号。
def do_foo(x,y):
    return x+y

A=[1,2,3,4]
a,*b,c=A
x=do_foo(*b)
print(x)