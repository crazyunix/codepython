#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: zuoyongyu_mingmingkongjian.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-15 12:48:25
#========================================================================
'''

j,k = 1,2
def proc1():
    j,k = 3,4
    print "proc1() # j == %d AND k == %d" % (j,k)
    k = 5

def proc2():
    j = 6
    proc1()
    print "proc2() # j == %d AND k == %d" % (j,k)
k = 7
proc1()
print "Global # J == %d AND k == %d" % (j,k)

j = 8
proc2()
print "Global # j == %d and k == %d" % (j,k)
