# 读取包中的数据文件
# 如果使用当前目录，python解释器无法控制当前目录
# 所以os.path.curdir是无法控制的

# 当时可以从__file__变量中获取这个文件的路径，但是当读取的数据是归档数据时，压缩了，open函数不管用
print(__file__)

# 另外，可以用pkgutil包来处理数据的读取
import pkgutil
data =pkgutil.get_data('chapter10','somedata.dat')
print(data)