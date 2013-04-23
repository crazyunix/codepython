#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: foo_bar.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-13 10:55:19
#========================================================================
'''
def foo():
    def bar():
        print 'Hello in bar ()'
    print 'Hello in foooooooo()'
    bar()
foo.__doc__ = 'Oops ,forgot to add doc str above!'
foo.version = 0.2
foo()
