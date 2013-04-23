#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: numConv.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-13 12:34:03
#========================================================================
'''
def convert(func,seq):
    'conv. sequence of numbers to same type'
    return [func(i) for i in seq]

myseq = (123,45.67,-6.2e8,99999999L)

print convert(int,myseq)
print convert(long,myseq)
print convert(float,myseq)
