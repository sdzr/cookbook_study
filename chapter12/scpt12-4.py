# 对临界区加锁
# 避免出现竞态条件（race condition）
# with 语句，自动加锁和释放

import threading

class SharedCounter:
    def __init__(self,initial_value=0):
        self.__value = initial_value
        self.__value_lock = threading.Lock()

    def incr(self,delta=1):
        with self.__value_lock:
            self.__value+=delta

# Rlock可重入锁，可实现类实例的共享，可保证每次都只有一个线程可使用类中的方法（无论创建了多少个实例）

_lock = threading.RLock
class SharedCounter_Rlock:
    def __init__(self, initial_value=0):
        self.__value = initial_value

    def incr(self, delta=1):
        with _lock:
            self.__value += delta


# Semaphore 是一种基于共享计数器的锁，可控制资源总数
# 例如限制并发总数

from threading import Semaphore
import urllib.request
_fetch_url_sema=Semaphore(5)

def fetch_url(url):
    
    with _fetch_url_sema:
        return urllib.request.urlopen(url)

