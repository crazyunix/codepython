#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: write_fn.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-11 14:32:13
#========================================================================
'''
import os

filename = raw_input('Please enter file name:')
fw = open(filename,'w')
while True:
    aline = raw_input('Please enter your input (.to quit) :')
    if aline != '.':
        fw.write('%s%s' % (aline,os.linesep))
    else:
        break

fw.close()
