#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: try_except_float.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-11 17:37:32
#========================================================================
'''
def float_num(num):
    try:
        reval = float(num)
    except ValueError:
        reval = '输入错了 你妹的！！！！'

    print reval
obj=raw_input('Please an float :')
if __name__ =='__main__':
    float_num(obj)
