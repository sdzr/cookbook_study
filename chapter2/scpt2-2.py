#在字符串开头或者结尾做字符串匹配
#方法一：
file_name_list=['a.txt','b.py','c.exe']
f=[v.startswith(('a','b')) for v in file_name_list]   #注意：此处的（'a','b'）只能用元组
print(f)
f=[v.endswith('.py') for v in file_name_list]
print(f)


#方法二：
file_name='abc.txt'
file_name_list[-4:]=='.txt'
#不优雅

#方法三：但是match只是从开头匹配
import re
file_name='http:dafsd'
pattern=r'https:|ftp:|http:'
f=re.match(pattern,file_name)
print(f.group())

#any函数的使用
