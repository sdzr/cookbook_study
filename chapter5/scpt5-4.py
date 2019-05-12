# 读写二进制数据
# 对于非二进制字符串，要编码为或解码

with open('tmp','wb') as f:
    f.write(b'hello world')
    f.write('hello world 2'.encode('utf8'))

# 读出来的每个字符所对应的字节整数值
with open('tmp', 'rb') as f:
    data=f.read()
    for c in data:
        print(c)
    # 解码
    dat = data.decode('utf8')
    for i in dat:
        print(i)

# 慎重使用
# 想数组，C结构体这样的对象，可以直接存储为二进制文件，还可以直接从文件读取到底层内存中
import array
a = array.array('i',[1,2,3,4,5])
with open('data.bin','wb') as f:
    f.write(a)
# 直接读取到内存中
a = array.array('i',[0,0,0,0])
with open('data.bin','rb') as f:
    f.readinto(a)
print(a)