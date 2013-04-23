#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: qiantao.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-14 18:02:20
#========================================================================
'''
def foo():
    m = 55
    def bar():
        n = 44
        print 'm + n = ' ,m + n

    print 'm is ',m
    bar()

foo()
