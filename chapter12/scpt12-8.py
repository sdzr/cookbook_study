# 实现简单的并行编程
# 如果进程提交后，获取result，则程序会阻塞到result语句这里，直到进程返回结果
# 任务必须定义为普通函数来提交，实例方法，闭包，或者其他可调用对象都不行
# 函数参数和返回值必须可兼容pickle编码，任务的执行是在单独的解释器中进行的，所以中间会用到进程通信，需要pickle序列化处理传递数据
# 提交的函数不应维持持久的状态或者副作用，最好是纯函数，不会修改系统环境，因为进程都是单独运行的，得保持事情简单干净
# Unix上是fork创建的，window是加载一个解释器的拷贝
# 进程和线程的结合使用，最好先创建加载进程池，然后在创建线程

import gzip
import io
import glob
from concurrent import futures


def find_robots(filename):

    robots=set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f,encoding='ascii'):
            fields = line.split()
            if fields[6]=='/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):

    files = glob.glob(logdir+'/*.log.txt')
    all_robots=set()
    with futures.ProcessPoolExecutor() as pool:
        for robot in pool.map(find_all_robots,files):
            all_robots.update(robot)
    return all_robots