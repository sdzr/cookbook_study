# 用命名空间来解析xml文档。
# 将命名空间包装到一个类当中

class XmlNamespace:

    def __init__(self,**kwargs):
        self.namespace={}
        for k,v in kwargs.items():
            self.register(k,v)

    def register(self,name,uri):
        self.namespace[name] = '{'+uri+'}'

    def __call__(self, path):
        return path.format_map(self.namespace)
# 知识点：__call__,类的实例，可以通过重载__call__方法，使得它变成一个可调用对象。_

ns = XmlNamespace(html='https//:www.baidu.com')
path = r'打开{html}'
print(ns(path))