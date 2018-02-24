#coding:utf-8
#author rongjing
#time 2018/2/23
#desc:

class ClassDecrator(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


if __name__ == '__main__':
    # TestObj = ClassDecrator()
    # TestObj.main()
    @ClassDecrator
    def bar():
        print('bar')

    bar()