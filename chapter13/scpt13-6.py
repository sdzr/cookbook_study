# 执行外部命令并获取输出
# 执行外部命令，然后把结果保存为一个python字符串
# 命令的执行不需要依赖底层的shell,直接传递给底层的系统
# shell=True则指定让shell来执行


import subprocess

try:
    out_bytes = subprocess.check_output(['netstat','-a'],timeout=3)
except subprocess.TimeoutExpired as e:
    print(e)
#print(repr(out_bytes.decode('utf8')))

# 如果执行不成功，则会返回一个非零的返回码，然后产生一个异常