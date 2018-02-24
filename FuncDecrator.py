#coding:utf-8
#author rongjing
#time 2018/2/23
#desc:装饰器的使用
import logging

def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warning("%s is running" % func.__name__)
        return func(*args, **kwargs)

    return wrapper

@use_logging
def foo():
    print("i am  foo")


@use_logging
def bar():
    print("i am  bar")

bar()