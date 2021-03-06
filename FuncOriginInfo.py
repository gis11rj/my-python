#coding:utf-8
#author rongjing
#time 2018/2/24
#desc:
from functools import wraps

def logged(func):
    @wraps(func)
    def with_logging(*args,**kwargs):
        print(func.__name__+" was called")
        return func(*args,**kwargs)
    return with_logging

@logged
def f(x):
    """does some math"""
    return x + x * x

print(f.__name__)
print(f.__doc__)