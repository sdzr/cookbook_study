# 通过重定向，管道或者输入文件作为脚本的输入

# filein.py
import fileinput

with fileinput.input() as f_input:
    for line in fileinput:
        print(line,end='')

# 调用方式
# ls | ./filein.py 管道
# ./filein.py /etc/passwd 文件
# ./filein.py < /etc/passwd 重定向

with fileinput.input('./ect/passwd') as f:
    for line in f:
        print(f.filename(),f.lineno(),line,end='')

