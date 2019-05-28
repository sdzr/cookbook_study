# 用函数替代只有单个参数的类

from urllib.request import urlopen

class UrlTemplate:
    def __init__(self, template):
        self.template=template

    def open(self,**kwargs):
        return urlopen(self.template.format_map(**kwargs))

# 用一个闭包的方式实现closure

def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(**kwargs))
    return opener