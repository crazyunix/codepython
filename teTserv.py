#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: teTserv.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-04-10 15:39:18
#========================================================================
'''


from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print '等待连接......'
    tcpCliSock,addr = tcpSerSock.accept()
    print '.....从连接: ',addr

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send('[%s] %s' %(ctime(),data))

        tcpCliSock.close()

tcpSerSock.close()
