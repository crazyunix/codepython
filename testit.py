#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: testit.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-15 14:49:18
#========================================================================
'''

def testit(func,*atuple,**adict):
    try:
        reval = func(*atuple,**adict)
        result = (True,reval)
    except Exception,diag:
        result = (False,str(diag))
    return result

def test():
    funcs = (int,long,float)
    valus = (123,123.0,'1234','12.34')

    for eachFunc in funcs:
        print '*' * 20
        for eachVal in valus:
            reval = testit(eachFunc,eachVal)
            if reval[0]:
                print '%s(%s) = ' %(eachFunc.__name__,eachVal),reval[1]
            else:
                print '%s(%s) = Failed: ' %(eachFunc.__name__,eachVal),reval[1]


if __name__ == '__main__':
    test()
