#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: global_foo.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-14 17:17:49
#========================================================================
'''
def foo():
    print '\ncalling foo()......'
    bar = 200
    print 'in foo(),bar is ',bar

bar = 100

print 'in __main__,bar is ',bar
foo()
print '\nin __main__,bar is (still)',bar
