#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: count_count.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-15 12:21:43
#========================================================================
'''
def counter(start_at=0):
    count = [start_at]
    def incr():
        count[0] += 1
        return count[0]
    return incr
