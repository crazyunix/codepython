#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: RoundFload.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-26 16:27:14
#========================================================================
'''
class RoundFloat(object):
    def __init__(self,val):
        "Value must be a float!!!!"
        self.value = round(val,2)


a = raw_input("Please input a number :")
xx =  RoundFloat(int(a))
print xx
