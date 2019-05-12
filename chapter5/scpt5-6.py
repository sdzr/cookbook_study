# 在字符串上执行IO操作
# 出于某种原因，需要模拟出一个普通文件
# StringIO和BytesIO
import io

s = io.StringIO()
s.write('hello world\n')
print(s)
print(s.getvalue())
