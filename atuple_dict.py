#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: atuple_dict.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-14 14:49:21
#========================================================================
'''
def print_string(title):
    print  title

def print_atuple(*atuple):
    print atuple

def print_adict(**adict):
    print  adict

print_string('a,b,c')
print_atuple('a,b,c')
print_adict(x=1,y=2)
