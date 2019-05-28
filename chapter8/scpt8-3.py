# 让对象支持上下文管理协议，通过with触发
# 需要实现__enter__,和__exit__方法,通过with语句来作为开关。
from socket import socket,AF_INET,SOCK_STREAM

class LazzConnection:
    def __init__(self,address,family=AF_INET,type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type=type
        self.scok=None

    def __enter__(self):
        if self.scok is not None:
            raise RuntimeError('Already connected')
        self.scok = socket(self.family,self.type)
        self.scok.connect(self.address)
        return  self.scok

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.scok.close()
        self.scok = None
