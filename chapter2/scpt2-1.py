#针对任意多的分割符拆分字符串
line='asf fsd; adf, dfa,dffg,  foo'
pattern=r'[;,\s]+'
import re
print(line)
s=re.split(pattern=pattern,string=line)
print(s)

#如果包含捕获组，那么匹配到的文本也会被包含进去
pattern=r'(;|,|\s)+'
print(re.split(pattern,line))