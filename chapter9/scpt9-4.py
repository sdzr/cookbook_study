# 定义一个可接受参数的装饰器

from functools import wraps
import logging

def logged(level,name=None,message=None):
    '''
    log decotator
    :param level:日志等级
    :param name: logger name
    :param message: log message
    :return:
    '''
    def decorato(func):
        logname=name if name else func.__module__
        log=logging.getLogger(logname)
        logmessage=message if message else func.__name__
        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,logmessage)
            return func(*args,**kwargs)
        return wrapper
    return decorato
@logged(logging.DEBUG)
def add(x,y):
    return x+y

print(3,4)