#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#========================================================================
#   FileName: ospatex.py
#     Author: Crazyunix
#      Email: crazyunix@163.com
#   HomePage: http://www.yunvi.com
# LastChange: 2013-03-11 15:46:59
#========================================================================
'''
import os
for tmpdir in ('/Users/liming/git/codepython'):
    if os.path.isdir(tmpdir):
        break
    else:
        print 'No temp directory avaiable !'
        tmpdir = ''

tmpdir = '/Users/liming/git/codepython'
if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print '** current temporary directory '
    print cwd

    print '** creating example directory ...'
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print '** new working directory....'
    print cwd

    print '___ original directory listing !'
    print os.listdir(cwd)

    print '## create test file !'
    fw = open('test','w')
    fw.write('Liming \n')
    fw.write('Yangyong \n')
    fw.write('Python \n')
    fw.write('123 123 123 123 \n')
    fw.close()

    print '** updated dirctory listing :'
    print os.listdir(cwd)

    print 'rename test to test.txt'
    os.rename('test','test.txt')
    print 'rename after dir 1111'
    print os.listdir(cwd)

    path = os.path.join(cwd,os.listdir(cwd)[0])
    print 'Full path'
    print path

    print '(pathname,basename)===='
    print os.path.split(path)

    print '(basename,extension )===='
    print os.path.splitext(os.path.basename(path))

    print '** displaing file contents ***'

    fr = open(path,'r')
    for i in fr:
        print i,

    fr.close()

    print '** delete file '
    os.remove(os.path.basename(path))
    print '*** update listdir now !'
    print os.listdir(os.path.dirname(path))
    print 'delete dirname !!! '
    os.rmdir(os.path.dirname(path))

