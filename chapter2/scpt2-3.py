#利用shell通配符做字符串匹配
#常见通配符有，(*.py,Dat[0-9]*.py)等
from fnmatch import  fnmatch,fnmatchcase
print(fnmatch('foo.txt','*.TXT'))

#fnmatch会与系统是否区分大小写保持一致

#如果想要严格区分大小写，可使用fnmatchcase
print(fnmatchcase('foo.txt','*.TXT'))
