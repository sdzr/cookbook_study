# 文本分词
# 知识点一：如何通过正则来个捕获组命名
import re
text = 'foo = 23 + 34*10'
NAME = r'(?P<NAME>[A-Za-z][a-zA-z0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>\=)'
WS = r'(?P<WS>\s+)'
master_patch = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_patch.finditer(text)
for i in scanner:
    print(i.group())
