# 让目录或者zip文件成为可运行脚本

# myapplication/
#     spam.py
#     ba.py
#     grok.py
#     __main__.py
#
# python3 myapplication
#
# 压缩后用 python myapplication.zip

# 只是添加了一个__main__.py文件，在运行的时候，会直接去运行这个文件
