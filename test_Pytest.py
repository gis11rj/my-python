#coding:utf-8
#author rongjing
#time 2018/2/24
#desc:

import pytest

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5

def test_wcf():
    assert inc(3) > 5

def test_hy():
    assert inc(3) < 5