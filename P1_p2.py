#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: P1_p2.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-21 16:12:45
#========================================================================
'''
class P1:
    def foo(self):
        print 'Called P1-foo'

class P2:
    def foo(self):
        print "Called P2-foo"
    
    def bar(self):
        print "Called P2-bar"

class C1(P1,P2):
    pass

class C2(P1,P2):
    def bar(self):
        print "Called C2-bar"

class GC(C1,C2):
    pass
