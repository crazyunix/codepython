#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: Parent_children.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-21 12:59:34
#========================================================================
'''
class P(object):
    '这是一个父类'
    def foo(self):
        print 'I am is 父类！'

class C(P):
    '这是一个子类'
    def foo(self):
        super(C,self).foo()
        print 'I am is 子类'
a = P()
b = C()
#a.foo()
b.foo()
