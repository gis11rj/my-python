#coding:utf-8
#author rongjing
#time 2018/2/26
#desc:

def tes_route(url_rule):
    def tes_decrator(f):
        print(f.__name__)
        return f
    return tes_decrator


@tes_route("url_rule")
def hello():
    print("def print hello")

