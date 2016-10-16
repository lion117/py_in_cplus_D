#!/usr/bin/env python    
# -*- coding: utf-8 -*
# Created by Leo on 2016/10/15.

import sys
import os
import shutil
import zipfile
import PyZipper




def beginPackagePy(t_dest_dir="",t_clean_cache= True):
    Py2CplusZipper.run(t_dest_dir, t_clean_cache)




class Py2CplusZipper:

    def __init__(self,t_dest_dir="" ,t_clean_cache = False):
        self._is_clean_cache = t_clean_cache
        self._sys_pydir_c ='C:/Python27/lib/'
        self._sys_pydir_d='D:/Python27/lib/'

        if len(t_dest_dir) ==0:
            t_dest_dir = os.getcwd()
        else:
            t_dest_dir = t_dest_dir.replace("\\", "/")
        if t_dest_dir.rfind("/") !=0 :
            t_dest_dir+= "/"
        self._temp_dir = t_dest_dir + "PyTemp"
        self._dest_zip = t_dest_dir + "python27.zip"

        if os.path.exists(self._temp_dir) is False:
            os.makedirs(self._temp_dir)
        if os.path.exists(self._dest_zip):
            os.remove(self._dest_zip)

    def getPythonModulesPath(self):
        i_list = []
        #sys.modules是一个字典，数据格式如下：
        #{'site': <module 'site' from 'D:\Python27\lib\site.pyc'>,
        for itor in sys.modules.itervalues() :
            str_itor = str(itor)
            if "from" in str_itor:
                data = str_itor.split("'")
                i_list.append(data[-2])
        return i_list

    def extractFiles(self, t_src_list):
        self._temp_dir.replace("\\", "/")
        if self._temp_dir.rfind('\\') != 0 or self._temp_dir.rfind('/') != 0:
            self._temp_dir += '/'
        for itor in t_src_list :
            i_dest = self.pyPathFilter(self._temp_dir, itor)
            self.copyFiles(i_dest, itor)


    def pyPathFilter(self,t_dest_dir, t_src_file):
        if len(t_src_file) ==0:
            raise ValueError("para could not be null")
            return
        t_src_file= t_src_file.replace("\\","/")
        i_lib_lenth = len(self._sys_pydir_c)

        if t_src_file.find(self._sys_pydir_c) != -1 or t_src_file.find(self._sys_pydir_d) != -1:
            i_temp = t_src_file[i_lib_lenth:]
            t_dest_dir += i_temp
        # users files
        else:
            print("user custmize files: "+ t_src_file)
            i_working = os.getcwd().replace("\\","/")
            if t_src_file.find(i_working) !=-1:
                t_dest_dir += t_src_file[len(i_working) +1:]
            else:
                # do not consider the folder if file not in working dir
                t_dest_dir += os.path.basename(t_src_file)
        return t_dest_dir

    def copyFiles(self,t_dest_file, t_src_file):
        if not os.path.isfile(t_src_file):
            print "error : file %s not exist!" % t_src_file
            return False
        if not os.path.exists(os.path.dirname(t_dest_file)):
            os.makedirs(os.path.dirname(t_dest_file))
        try:
            shutil.copy2(t_src_file, t_dest_file)
            print "copy file : %s to %s" % (t_src_file, t_dest_file)
        except IOError ,ex:
            print "error : copy %s to %s faild : %s" % (t_src_file, t_dest_file, ex)
            return False
        return True

    def clean(self):
        if self._is_clean_cache is False:
            return
        if os.path.isdir(self._temp_dir) is True:
            shutil.rmtree(self._temp_dir)


    def copyPydll(self):
        i_dest_dll= os.path.dirname(self._dest_zip) + "/python27.dll"
        print i_dest_dll
        if os.path.exists(i_dest_dll):
            return # dll had been exist
        i_src_dll_D="D:/Python27/python27.dll"
        i_src_dll_C="C:/Python27/python27.dll"
        if os.path.exists(i_src_dll_C):
            shutil.copy2(i_src_dll_C, i_dest_dll)
        elif os.path.exists(i_src_dll_D):
            shutil.copy2(i_src_dll_D,i_dest_dll)
        else:
            print("not find python27.dll in default path")



    @staticmethod
    def run(t_dest_dir="",t_clean_cache= True):
        i_this = Py2CplusZipper(t_dest_dir,t_clean_cache)
        i_module_list = i_this.getPythonModulesPath()
        i_this.extractFiles(i_module_list)
        PyZipper.pyZipFile(i_this._temp_dir, i_this._dest_zip)
        #i_this.copyPydll()
        i_this.clean()

    @staticmethod
    def main():
        i_this = Py2CplusZipper("D:\System\Desktop",False)
        i_module_list = i_this.getPythonModulesPath()
        i_this.extractFiles(i_module_list)
        PyZipper.pyZipFile(i_this._temp_dir, i_this._dest_zip)
        i_this.copyPydll()
        i_this.clean()


    _sys_pydir_c = ""
    _sys_pydir_d = ""
    _temp_dir = ""
    _dest_zip = ""
    _is_clean_cache= False







if __name__ == "__main__":
    beginPackagePy()
    pass