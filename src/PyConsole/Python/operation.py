# -*- coding: utf-8 -*-
"""
Created on Sun May 11 16:55:07 2014

@author: LEO
"""

import os
import sys
import shutil


def elimitcopy(folderpath):
    for dirpath, dirnames, filenames in os.walk(folderpath):
        for onefile in filenames:
            if os.path.splitext(onefile)[1]=='.py':
                myfile=os.path.join(dirpath,onefile)
                copyfile=os.path.splitext(onefile)[0]+'.pyc'
                iscopyfile=os.path.join(dirpath,copyfile)
                if os.path.isfile(iscopyfile) is True:
                    os.remove(myfile)
                    print myfile
                    return True # make sure the file is a copy
                else :
                    return False








def deltempdir(dirpath):
    if os.path.isdir(dirpath) is True:
        shutil.rmtree(dirpath)
        return True
    else:
        return False



if __name__=='__main__':
    dirpath='C:/Users/LEO/Desktop/pykag/'
    if elimitcopy(dirpath):
        if deltempdir(dirpath):
            print 'work have been done'
        else:
            print 'folder delete failed'
    else:
        print 'file .py delete failed'