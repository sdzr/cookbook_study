# 解析命令行选项
# 解析argc，argv，然后将参数存储到dest所对应的变量中

import argparse

parser = argparse.ArgumentParser(description='Search some files')
parser.add_argument(dest='filenames',metavar='filename',nargs='*')
