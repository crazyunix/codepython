#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: pc_init.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-21 15:15:35
#========================================================================
'''
class P(object):
    def __init__(self):
        print 'Calling P '

class C(P):
    def __init__(self):
        #P.__init__(self)
        super(C,self).__init__()
        print "Calling CCCCC"


c = C()
#p =P()
