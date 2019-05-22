# 编码和解码十六进制数字
import binascii

s = b'hello'
print(s)

h = binascii.b2a_hex(s)

print(h)

p = binascii.a2b_hex(h)

print(p)