#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: filename.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-11 12:46:14
#========================================================================
'''
filename = raw_input("Please an file :")
data = open(filename,'r')
nr = data.readlines()
data.close()
print '--'*20
for i in  nr:
    print i,

print '*' * 40
