#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: Hotrom.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-20 16:02:01
#========================================================================
'''
def HotelRoomCalc(object):
    'Hotel room calcuator'
    def __init__(self,rt,rm=0.1,sale=0.085):
        self.sale = sale
        self.roomTax = rm
        self.roomRate = rt
    def calcTotal(self,days=1):
        daily = round((self.roomRate*(1 +self.roomTax + self.sale)),2)
        return float(days) * daily

