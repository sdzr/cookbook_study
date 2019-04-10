# 将Unicode统一表示为规范形式
# unicodedata包的使用，可以用来规范化Unicode字符串和Unicode字符串类型检测
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalape\u0303o'
print(s1)
print(s2)
print(s1==s2)
print(len(s1),len(s2))
# 显然这会造成Unicode不规范,其中第一个那个字符由全组成，后一个是由两个字符组成。


# 为了解决这个问题
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))
# NFC表示字符全组成，NFD表示每一个字符都应该是完全分开的，由其他字符拼接成的

print([c for c in t1 if not unicodedata.combining(c)]) # combine可以判断一个字符是否为组合字符。




