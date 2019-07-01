# 定义一个Actor任务

# 采用所谓的Actor模式编程
#  一种最简单的用来解决并发和分布式编程的方法之一
# 由于消息发送到一个中间的存储中，所以属于单向且异步的，发送者并不知道接受者何时接收到，任务是否完成。

from queue import Queue
from threading import Thread,Event
import logging

logger = logging.getLogger('mylog')
logger.setLevel(logging.DEBUG)

fch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fch.setFormatter(formatter)

logger.addHandler(fch)



class ActorExit(Exception):
    pass


class Actor:
    def __init__(self):
        self._mailbox=Queue()

    def send(self,msg):
        self._mailbox.put(msg)

    def recv(self):
        msg=self._mailbox.get()
        if msg is ActorExit:
            print('exit')
            raise   ActorExit()
        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        self._terminated = Event()
        print('Event')
        t = Thread(target=self._bootstrap)
        print('Event after')
        t.daemon = True
        t.start()
        print('zz')

    def _bootstrap(self):
        try:
            print('run before')
            self.run()
            print('run')
        except ActorExit:
            pass
        finally:
            print('set')
            self._terminated.set()
            print('set after')
    def join(self):
        print('wait')
        self._terminated.wait()
        print('wait afer')

    def run(self):
        while True:
            print('sss')
            msg = self.recv()

class PrintActor(Actor):
    def run(self):
        while True:
            print('ok')
            msg = self.recv()
            logger.warning(msg)
            print('Got:',msg)

p =PrintActor()
p.send('Hello')
p.send('world')
p.start()

p.close()
p.join()