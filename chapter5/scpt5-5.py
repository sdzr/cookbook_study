# 对已不存在的文件进行读写操作
# 即解决了意外覆盖已存在问题的问题
# 用xt代替wt，若文件已存在，则报错,而不是覆盖

with open('data.bin','xb') as f:
    f.write(b'hello world')

