# -*- coding: utf-8 -*-
"""
Created on Fri May 30 15:35:47 2014

@author: LEO
"""
import os

def sayhi():
    print "hello world"
    print os.getcwd()

def find_targetfolder():
    strpath=os.getcwd()
    upperpath= os.path.split(strpath)[0]
    upperpath+='\\Release\\'
    if os.path.isdir(upperpath) is True:
        return upperpath

    else :
        return None



if __name__=="__main__":
#    sayhi()
    find_targetfolder()