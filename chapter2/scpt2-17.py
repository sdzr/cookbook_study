#  想要将xml或者HTML中的实体如（<,>,&）等替换成他们所对应的文本，或者反之
import xml
from html.parser import HTMLParser
from xml.sax.saxutils import unescape

# 省略 