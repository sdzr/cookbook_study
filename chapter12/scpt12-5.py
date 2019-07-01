# 避免死锁
# 如果一个线程需要获取不止一把锁，则可能会出现死锁

# 解决方案：给每一个锁分配一个数字序号，并且在获取多个锁的时候，只能按升序的方式来获取

import threading
from contextlib import contextmanager

_local = threading.local()
@contextmanager
def acquire(*locks):
    locks = sorted(locks,key=lambda x:id(x))
    acquired = getattr(_local,'acquired',[])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    acquired.extend(locks)
    try:
        _local.acquired=acquired
    except Exception as E:
        print(E)
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]

x_lock=threading.Lock()
y_lock=threading.Lock()

def thread_1():
    while True:
        with acquire(x_lock,y_lock):
            print('Thread-1')
def thread_2():
    while True:
        with acquire(y_lock,x_lock):
            print('Thread-2')

t1=threading.Thread(target=thread_1)
t1.daemon=True
t1.start()

t2=threading.Thread(target=thread_2)
t2.daemon=True
t2.start()
