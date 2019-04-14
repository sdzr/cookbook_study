# 这一节主要学会使用translate函数进行批量映射（替换）

s = 'python\fis\tawesome\r\n'
print(s)
remap = {
    ord('\f'): ' ',
    ord('\t'): ' ',
    ord('\r'): None
}
print(s.translate(remap))
