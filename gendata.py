#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: gendata.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-04-09 14:47:26
#========================================================================
'''

from random import randint,choice
from string import lowercase
from sys import maxint
from time import ctime


doms = ('com','edu','net','org','gov')

for i in range(randint(5,8)):
    dtint = randint(0,7002581251)
    dtstr = ctime(dtint)

shorter = randint(4,7)
em = ''

for i in range(shorter):
    em += choice(lowercase)

longer = randint(shorter,12)

dn = ''
for i in range(longer):
    dn += choice(lowercase)

print '%s::%s@%s.%s::%d-%d-%d' %(dtstr,em,dn,choice(doms),dtint,shorter,longer)
