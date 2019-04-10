# 编写多行模式的正则表达式
# 如果一段文字共有多行，包含换行符，在匹配的时候会出问题
import re
comment = re.compile(r'/\*(.*)\*/')
text1 = '/* This is a commet */'
text2 = '''/* This is a
multiline comment */'''
print(comment.findall(text1))
print(comment.findall(text2))

# 要解决这个问题，需要用到一个新的正则符号 （？：...）制定一个非捕获组，只做匹配而不捕获，也不会分配组号
comment1 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment1.findall(text1))
print(comment1.findall(text2))

# 另外，re中还有一个有用的标记，re.DOTALL,是的正则表达式（.）可以匹配所有的字符，包括\n。
comment = re.compile(r'/\*(.*)\*/',re.DOTALL)
print(comment.findall(text1))
print(comment.findall(text2))