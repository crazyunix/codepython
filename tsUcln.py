#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: tsUcln.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-04-11 11:21:42
#========================================================================
'''
from socket import *
HOST='192.168.10.72'
PORT=51251
BUFSIZE=1024
ADDR=(HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>>>')
    if not data:
        break
    udpCliSock.sendto(data,ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print data,udpCliSock.close()

udpCliSock.close()
