#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: create_class.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-18 12:31:22
#========================================================================
'''
class AddrBookEntry(object):
    'Address book entry class'
    
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        print 'Created instance for :' ,self.name

    def updatePhone(self,newph):
        self.phone = newph
        print 'Update your phone for:',self.phone

class EmailAddrBookEntry(AddrBookEntry):
    'add email id entyr class'

    def __init__(self,nm,ph,em,id):
        AddrBookEntry.__init__(self,nm,ph)
        self.email = em
        self.id = id

    def UpdateEmail(self,newem):
        self.email = newem
        print 'Update email address for :',self.name
