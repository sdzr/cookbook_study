# 编写装饰器为包装的函数添加参数
# 使用keyword-only 参数将额外的参数注入到函数

from functools import wraps
import inspect

def optional_debug(func):
    # 防止参数已存在
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined!')

    @wraps(func)
    def wrapper(*args,debug=False,**kwargs):
        if debug:
            print('calling',func.__name__)
        return func(*args,**kwargs)

    # 保证参数签名正确反映出增加的参数
    sig = inspect.signature(func)
    parms=list((sig.parameters.values()))
    parms.append(inspect.Parameter('debug',inspect.Parameter.KEYWORD_ONLY,default=False))
    wrapper.__signature__=sig.replace(parameters=parms)
    return wrapper

@optional_debug
def add(x,y):
    return x+y

print(inspect.signature(add))
print(add(2,3,debug=True))