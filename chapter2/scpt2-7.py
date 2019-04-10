#由于python在做正则匹配的时候，默认的都是贪婪匹配
#当想要最短的匹配的时候

import re
pattern = r'\"(.*)\"'
text = 'Computer says "no." Phone says "Yes."'
ans = re.findall(pattern, text)
print(ans)

#将pattern做一个小修改即可最短匹配
#在*后面加上+或者？，可以将匹配算法强制调整为最短匹配

pattern = r'\"(.*?)\"'
text = 'Computer says "no." Phone says "Yes."'
ans = re.findall(pattern, text)
print(ans)