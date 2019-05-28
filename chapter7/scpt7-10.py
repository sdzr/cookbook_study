# 在回调函数中携带额外的状态
# 一般有3种方式
# 1.在类实例上携带状态参数
# 2.在闭包函数上携带状态参数
# 3.协程实现，通过send给协程交换数据，传数据给yield，在通过yield返回数据

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)