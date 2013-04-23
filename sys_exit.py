#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: sys_exit.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-04-08 10:32:35
#========================================================================
'''
import sys

def usage():
    print "at least 2 arguments (inc1. cmd name)."
    print 'usage: args.py arg1 arg2 [arg3...]'
    sys.exit(1)

argc = len(sys.argv)
if argc < 3:
    usage()

print "Number of args entered:",argc
print "args (inc1,cmd name)were:",sys.argv
