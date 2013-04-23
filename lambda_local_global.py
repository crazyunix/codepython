#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: lambda_local_global.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-15 12:41:02
#========================================================================
'''
x = 10
def foo():
    y = 5
    bar = lambda z:x + z
    print bar(y)
    y = 8
    print bar(y)

if __name__ == '__main__':
    foo()
