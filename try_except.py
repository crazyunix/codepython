#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: try_except.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-11 17:30:04
#========================================================================
'''
ff = raw_input('Please enter a file :')
try:
    fr = open(ff)
except Exception,e:
    print e

