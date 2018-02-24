#coding:utf-8
#author rongjing
#time 2018/2/23
#desc:带参数的装饰器的使用
import logging

def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.warning("%s is running" % func.__name__)
            logging.warning("level is %s" % level)
            return func(*args, **kwargs)

        return wrapper
    return decorator

@use_logging(level="warn")
def foo(name='foo'):
    print("i am  %s"%name)


@use_logging
def bar():
    print("i am  bar")

foo()