# 将字典转换为xml


from xml.etree.ElementTree import Element,tostring
'''
turn a simle dict of ket/value into xml
'''
def dict_to_xml(tag,d):
    elem = Element(tag)
    for key,val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem
s = {'name':'GooG','shares':100,'price':490.1}

e=dict_to_xml('stock',s)
print(tostring(e))


#  不要尝试手工创建xml
#  这样还要处理特殊字典
from xml.sax.saxutils import escape,unescape
print(escape('<spam>'))
# print(unescape(_))