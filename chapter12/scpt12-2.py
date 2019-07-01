# 判断线程是否已经启动
# 对一个已经加载的线程，想知道它什么时候开始运行

# 采用Event对象，当对象被设置的时候，线程才会从等待阻塞的状态被唤醒

from threading import Thread,Event
import time

def countdown(n,start_evt):
    print('countdown starting')
    start_evt.set()
    while n>0:
        print('T-minus',n)
        n=n-1
        time.sleep(3)

start_evt=Event()

print('Launching coubtdown')
t = Thread(target=countdown,args=(10,start_evt))

t.start()

# 在这儿等set点
start_evt.wait()

print('countdown is running')
