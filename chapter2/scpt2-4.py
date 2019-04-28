#文本模式的匹配和查找
#方法一：使用startwith和endwith
text='abc.txt'
print(text.startswith('abc'),text.endswith('.txt'))

#方法二：使用re模块
import re
text='11/12/2017:abc'
#re.match函数，只会匹配字符串的头部
pattern=r'\d+/\d+/\d+'
print(re.match(pattern,text))

#如果后面会一直用固定的pattern来匹配，可以将pattern编译一下，由于re模块的函数会对pattern模块缓存，所以编译与否，并不会有巨大的性能差异
patt=re.compile(pattern)
print(patt.match(text))

#如果想要匹配出文本中所有的项，可以用re.findall
text='11/12/2017:abc:24/10/2018'
print(patt.findall(text))

#也可以用捕获组，将内容单独提取出来
pattern=r'(\d+)/(\d+)/(\d+)'
patt=re.compile(pattern)
print(patt.findall(text))
print(patt.match(text).groups())

#findall返回的是一个list，如果想要返回一个迭代器，怎用finditer
print(patt.finditer(text))