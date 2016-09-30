# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 20:53:51 2014

@author: LEO
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 20:26:09 2014

@author: LEO
"""
import sys
import os
import threading
sys.path.append('./pymodule/')
from  usermodule import *
#from PyQt4 import QtCore, QtGui


def  second():
    print '============='
    print 'hi, this is the second files in test '
    print '============='

def second_user():
    use_module_sayhi()

def second_thread():
    ak=threading.Thread()
    print 'threading is calling'


if __name__=='__main__':
    second_user()
    second_thread()

