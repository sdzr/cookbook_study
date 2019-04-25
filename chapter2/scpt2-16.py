# 固定列数重新格式化文本
import textwrap
import os

s = r'Thanks to the flexibility of Python and the powerful ecosystem of packages, the Azure CLI supports features such as ' \
    r'autocompletion (in shells that support it), persistent credentials, JMESPath result parsing, lazy initialization, ' \
    r'network-less unit tests, and more.Building an open-source and cross-platform Azure CLI with Python by Dan TaylorUse ' \
    r'Python for…MoreWeb Development: Django, Pyramid, Bottle, Tornado, Flask, web2pyGUI Development: tkInter,' \
    r' PyGObject, PyQt, PySide, Kivy, wxPython'
print(textwrap.fill(s, 30))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 70, initial_indent = ' '))


print(os.get_terminal_size())