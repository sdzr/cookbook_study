# 通过名称来查找文件

import os

def findfile(start,name):
    for relpath,dirs,files in os.walk(start):
        print(relpath,dirs,files)
        if name in files:
            full_path = os.path.join(start,relpath,name)
            print(os.path.normpath(full_path))
            print(full_path)

if __name__ =='__main__':
    findfile(r'C:\Users\sdzr\PycharmProjects\cookbook_study\chapter13','scpt13-1.py')
