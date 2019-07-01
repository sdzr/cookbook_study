# 创建线程池

# 解决方法1：
from socket import socket,AF_INET,SOCK_STREAM
from concurrent.futures import ThreadPoolExecutor

def echo_client(sock,client_addr):
    print('Got connection from',client_addr)
    while True:
        msg=sock.recv(65535)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')
    sock.close()

def echo_server(addr):
    pool=ThreadPoolExecutor(128)
    sock = socket(AF_INET,SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock,client_addr=sock.accept()
        a=pool.submit(echo_client,client_sock,client_addr)
        print(a.result())

echo_server(('',15000))

# 方案二是：使用队列，创建很多线程，利用队列get的阻塞，是的线程等在那里，然后往队列里面put连接，然后线程跑起来
# 但一般不见手工实现，不容易取得线程跑完的结果，
# 详情518
