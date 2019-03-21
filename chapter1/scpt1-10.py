#去除列表中的重复项，但是不改变元素的顺序
#若直接使用set来处理列表，会改变元素的顺序

def dedupe(items):
    s=set()
    for item in items:
        if item not in s:
            yield item
            s.add(item)
#但是当列表中的元素不可哈希时，即元素是可变元素时不可哈希
#整数，浮点数，元组，字符串都是不可变的，可以哈希，dict就不可以，因为value可变

#通过加一个key参数，可以解决元素不可哈希的问题，例如dict，对于复杂的不可哈希元素，可以按照元素的某个字段或者属性去重
#key可以是个lambda函数.

def dedupe(items,key):
    s=set()
    for item in items:
        val=item if key is None else key(item)
        if val not in s:
            yield item
            s.add(val)

