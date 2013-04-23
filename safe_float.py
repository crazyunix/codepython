#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: safe_float.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-12 14:53:11
#========================================================================
'''
def safe_float(num):
    try:
        retval = float(num)
    except (ValueError,TypeError),diag:
        retval = str(diag)

    print retval
obj = raw_input('Please enter float:')
if __name__ == '__main__':
    safe_float(obj)
