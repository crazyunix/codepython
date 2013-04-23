#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: filter_randint.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-14 15:57:44
#========================================================================
'''
from random import randint

def odd(n):
    return n % 2

all = []
for i in range(9):
    all.append(randint(1,99))
print all
print filter(odd,all)

xall = []
for i in range(9):
    xall.append(randint(1,99))
print filter(lambda x: x%2, xall)
print 'aaa'
print (x for x in xall if x % 2)
