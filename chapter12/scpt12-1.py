# 启动和停止线程

import time
import  threading

def countdowmn(n):
    while n> 0:
        print('T-minus',n)
        n=n-1
        time.sleep(5)

t = threading.Thread(target=countdowmn,args=(10,))
# 在start之前只是创建了线程实例，还不会运行
# 一旦线程创立以后就完全由操作系统处理，独立运行，直到目标函数返回为止
t.start()

# 查看线程是否还在运行
if t.is_alive():
    print('running')
else:
    print('Completed')

# join可以请求连接到某个线程上，这么做会等待该线程的结束
t.join()

# 对于需要长时间运行的线程或者一直不断运行的后台任务，
# 应该考虑设置守护线程daemon
# 设置了守护线程的线程是无法被连接的，当主线程结束后会自动销毁
t=threading.Thread(target=countdowmn,args=(5,),daemon=True)
t.start()


# 终止线程的一种编程实现
class CountdownTask:
    def __init__(self):
        self.__running=True

    def terminate(self):
        self.__running=False

    def run(self,n):
        while n > 0:
            print('T-minus',n)
            n=n-1
            time.sleep(3)

c= CountdownTask()
t=threading.Thread(target=c.run,args=(5,))
t.start()
c.terminate()
t.join()


# 由于GIL的限制，不应该使用线程来处理计算密集型任务
# python线程比较适合用来处理I/O，以及涉及到阻塞的问题

# 下面是一个线程I/O阻塞的处理方法，设置一个超时循环

class IOTask:
    def terminate(self):
        self.__running=False

    def run(self,sock):
        sock.settimeout(5)
        while self.__running:
            try:
                data=sock.recv(8192)
            except sock.timeout:
                continue
        return