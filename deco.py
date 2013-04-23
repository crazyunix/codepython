#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: deco.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-13 12:20:28
#========================================================================
'''
from time import ctime,sleep

def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' %(ctime(),func.__name__)
        return func()
    return wrappedFunc

@tsfunc
def foo():
    pass

foo()
sleep(4)


for i in range(2):
    sleep(1)
    foo()
