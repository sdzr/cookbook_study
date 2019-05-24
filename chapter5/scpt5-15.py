# 打印无法解码的文件名
# 就是一些文件名无法被打印出来


def bad_filename(filename):
    return repr(filename)[1:-1]


files = []
for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))
