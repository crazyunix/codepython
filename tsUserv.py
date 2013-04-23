#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: tsUserv.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-04-11 11:15:44
#========================================================================
'''
from socket import *
from time import ctime

HOST='192.168.10.73'
PORT=51251
BUFSIZE=1024
ADDR=(HOST,PORT)


udpSock = socket(AF_INET,SOCK_DGRAM)
udpSock.bind(ADDR)

while True:
    print "等待传输消息。。。"
    data,addr = udpSock.recvfrom(BUFSIZE)
    upSock.sendto('[%s] %s' % (ctime(),data),addr)
    print ".......received from and returned to:",addr

udpSock.close()
