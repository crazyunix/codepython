#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: mozilla.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-04-11 16:00:00
#========================================================================
'''

import ftplib
import os
import socket


#HOST='ftp.mozilla.org'
#DIRN='pub/mozilla/releases/m18/'
#FILE='README'
HOST='192.168.10.72'
DIRN='pub'
FILE='liming'
def main():
    try:
        f = ftplib.FTP(HOST)
    except(socket.error,socket.gaierror),e:
        print "ERROR:cannot rech %s" % HOST
        return
    print '*** connected to host "%s"' % HOST
    try:
        f.login()
    except ftplib.error_perm:
        print "ERROR: cannot to login anonymously "
        f.quit()
        return

    print '*** login in as "anonymous"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print "Error:cannot CD to '%s'" % DIRN
        f.quit()
        return
    print '*** changed to "%s"' % DIRN

    try:
        f.retrbinary('RETR %s' % FILE,open(FILE,'wb').write)
    except ftplib.error_perm:
        print "Error :cannot to read file '%s'" % FILE
        os.unlink(FILE)
    else:
        print "*** Download %s to CWD " % FILE
    f.quit()
    return


if __name__ == '__main__':
    main()
