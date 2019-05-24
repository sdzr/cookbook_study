# Base64编码解码
import base64

s = b'hello'

a = base64.b64encode(s)
print(a)
b = base64.b64decode(a)

print(b)
