# -*- coding: utf-8 -*-
"""
Created on Thu May 29 15:27:20 2014

@author: LEO
"""


import os
import shutil

def sayhi():
    print "hello world"

def del_folder(strpath):
    '''
    return value representation :
    0  # do nothing , file exist
    1  # delete folder
    2   # no find the folder
    '''
    handle=folder_operation(strpath)
    return handle.execute()

class folder_operation(object):
    def __init__(self,strpath):
        self.folderpath=strpath
        self.file_ext='.txt'

    def execute(self):# one key to delete
        if self.seek_folder():
            if self.seek_file():
                return 0  # do nothing , file exist
            else:
                return 1  # delete folder

        else:
            print 'not find the folder'
            return 2   # no find the folder


    def seek_folder(self):
        if os.path.exists(self.folderpath):
            return True
        else:
            return False

    def seek_file(self):
        for dirpaht, dirname, filenames in os.walk(self.folderpath):
            if filenames.__len__():
                for file_name in filenames:
                    if os.path.splitext(file_name)[1]==self.file_ext:
                        print 'file exist , do nothing '
                        return True
                    else:
                        #delete the folder
                        print self.folderpath,"folder have been deleted"
                        self.delete_folder(self.folderpath)
                        return False
            else:
                print 'find no file in folder'
                self.delete_folder(self.folderpath)
                return False

    def delete_folder(self, strpath):
            shutil.rmtree(strpath)# delete the dir
            print  self.folderpath , 'have been deleted'




if __name__=="__main__":
   del_folder('d:/test/')
