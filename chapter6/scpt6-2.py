# 读写json数据
import json


data = {'name':'ACME',
        'shares':100,
        'price':542.35
        }
json_str = json.dumps(data)
print(json_str)
dat = json.loads(json_str)

print(dat)
# 转到文件
with open('data.json','w') as f:
    json.dump(data,f)
with open('data.json','r') as f:
    data = json.load(f)
print(data)

# 按字母顺序打印字典元素
from pprint import pprint
pprint(data)

# 将json数据解码为有序字典
from collections import OrderedDict
# 一个json字符串
data = '{"name":"ACME","shares":50,"price":109.35}'
dat = json.loads(data,object_pairs_hook=OrderedDict)
print(dat)

# 将json转变为python对象
class JsonStr:
    def __init__(self,d):
        self.__dict__=d

dat =json.loads(data,object_hook=JsonStr)
print(dat.name)

# 只是为了好看点，存起来
print(json.dumps(data,indent=4))
print(json.dumps(data,sort_keys=True))

# 类实例是无法存为JSON的
# 如果想实例化类实例，可以提供一个函数，将类实例作为输入，返回一个序列化处理的字典

classes={'JsonStr':JsonStr}


def serialize_instance(obj):
    d= {'__classname__':type(obj).__name__}
    d.update(vars(obj))
    return d
# 反序列化，返回一个类，如果传入的字典含有'__classname__',则说明它是一个类
def unserialize_instance(d):
    clsname=d.pop('__classname__',None)
    if clsname:
        cls=classes[clsname]
        obj = cls.__new__(cls)
        for k,v in d.items():
            setattr(obj,k,v)
        return obj
    else:
        return d
