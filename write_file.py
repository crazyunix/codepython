#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: write_file.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-20 12:36:23
#========================================================================
'''
import time
def Write_log():
    fp = open('log','w')
    for i in range(0,10):
        a = str(i) + "######" + time.strftime("%Y") +"\n"
        fp.write(str(a))
    fp.write("\n")
    fp.close()

def Read_log():
    fp = open('log','r')
    all = fp.readlines()
    fp.close
    for i in all:
        print i,time.strftime("%Y:%m:%d:%H:%M")


if __name__ == '__main__':
    Write_log()
    Read_log()
