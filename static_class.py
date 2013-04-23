#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: static_class.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-21 11:51:10
#========================================================================
'''
'''staticmethod and classmethod'''

class Teststaticmethod:
    @staticmethod
    def foo(self):
        print '在静态方法中！！！！'
        print 'foo() static method is :',self.__name__

class Testclassmethod:
    @classmethod
    def foo(cls):
        print '在类方法中！！！！！！！！！'
        print 'foo() class is :',cls.__name__
Teststaticmethod.foo('test')
Testclassmethod.foo()
