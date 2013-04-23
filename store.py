#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: store.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-14 12:57:19
#========================================================================
'''
def store(data,full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1,' ')
        labels = 'first','middle','last'

for label,name zip(labels,names):
    people = lookup(data,label,name)

    if people:
        people.append(full_name)
    else:
        data([label][name]) = [full_name]

store()

