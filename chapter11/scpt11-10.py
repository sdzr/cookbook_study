# 为网络服务增加SSL支持
# 服务器与客户端通过SSL进行身份验证并对数据传输进行加密
# 内容太多，要详细去了解

from socket import socket,AF_INET,SOCK_STREAM
import ssl

KEYFILE = 'server_key.pem'
CERTFILE = 'server_cert.pem'

def echo_client(s):
    while True:
        data=s.recv(8192)
        if data ==b'':
            break
        s.send(data)
    s.close()
    print('Connection closed')

def echo_server(address):
    s = socket(AF_INET,SOCK_STREAM)
    s.bind(address)
    s.listen(1)
    s_ssl = ssl.wrap_socket(s,keyfile=KEYFILE,certfile=CERTFILE,server_side=True)
    while True:
        try:
            c,a = s_ssl.accept()
            print('Got connection',c,a)
            echo_client(c)
        except Exception as e:
            print('{}:{}'.format(e.__class__.__name__,e))

echo_server(('',20000))
