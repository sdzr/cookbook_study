#以区分大小写大的方式对文本做查找和替换
text='UPPER PYTHON ,lower python,Mixed Python'
import re
t1=re.findall('PYTHON',text,flags=re.IGNORECASE)
print(t1)

t2=re.sub('python','snake',text,flags=re.IGNORECASE)
print(t2)

#当想要替换的词在替换之后也按照被替换词的大小写格式替换时，可以写一个支持函数,传入一个参数后，再返回一个需要参数的函数
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

t3=re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)

print(t3)