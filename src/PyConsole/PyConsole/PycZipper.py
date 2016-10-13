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
import shutil
import zipfile


def sayhi():
    print "PycZipper begin to work"


######################################
#下面所有部分是相关的pyc抽取函数
#获得程序中所有模块的路径
def getPythonModulesPath():
    lst = []
    #sys.modules是一个字典，数据格式如下：
    #{'site': <module 'site' from 'D:\Python27\lib\site.pyc'>,
    for v in sys.modules.itervalues() :
        s = str(v)
        if "from" in s:
            data = s.split("'")
            lst.append(data[-2])
        else :
            print "module : ", s
    return lst

#抽取文件
def extractFiles(t_dest_dir, t_src_list):
    t_dest_dir.replace("\\", "/")
    if t_dest_dir.rfind('\\') != 0 or t_dest_dir.rfind('/') != 0:
        t_dest_dir += '/'


    for itor in t_src_list :
        i_dest = filiterPath(t_dest_dir, itor)
        print i_dest +'   '+itor
        # copyFiles(i_dest, itor)

#过滤路径 去掉最大绝对路径
def filiterPath(t_dest_dir, t_src_file):
    dest = t_dest_dir
    maxLen = 0
    for itor_path in sys.path:
        i_len = len(itor_path)
        if i_len < len(t_src_file) and itor_path == t_src_file[:i_len]:
            if maxLen < i_len:
                dest = t_dest_dir + t_src_file[i_len + 1:]
                maxLen = i_len

    dest.replace("/", "\\")
    if '.' in dest: #去掉文件名
        p = dest.rfind('\\')
        if p >= 0:
            dest = dest[:p]
    return dest

#拷贝文件
#如果目标路径不存在，则创建
def copyFiles(destDir, srcFile):
    if not os.path.isfile(srcFile):
        print "error : file %s not exist!" % srcFile
        return False
    if not os.path.isdir(destDir):
        os.mkdir(destDir)
        print "make dir:", destDir
    try:
        shutil.copy2(srcFile, destDir)
        print "copy file : %s to %s" % (srcFile, destDir)
    except IOError:
        print "error : copy %s to %s faild" % (srcFile, destDir)
        return False
    return True


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

def deleteTemps(dirpath):
    if os.path.isdir(dirpath) is True:
        shutil.rmtree(dirpath)
        return True
    else:
        return False


def cpy_py27dll():
    res_file='E:/baiducloud/Additon library/dll/python27.dll'

    des_path=find_targetfolder()
    if des_path is None:
        print 'the python27.dll did not copy to the specialy folder ,please check whether the dir exist'
        print 'error', des_path
    else:# copy the py27dll to the folder
        shutil.copy2(res_file, des_path)



def find_targetfolder():
    strpath=os.getcwd()
    upperpath= os.path.split(strpath)[0]
    upperpath+='\\Release\\'
    if os.path.isdir(upperpath) is True:
        return upperpath
    else :
        return None


def pyzipfiles():
    i_module_path = getPythonModulesPath()
    i_dest_zip= "C:/Users/LEO/Desktop/python27.zip"
    i_temp_folder= "C:/templefolder"
    extractFiles(i_temp_folder, i_module_path)

    elimitcopy(i_temp_folder)
    argv = ("-c", i_dest_zip, "src", i_temp_folder)
    zipfile.main(argv)
    cpy_py27dll()  # copy the python27.dll to the foledr
    ultipath=find_targetfolder()
    if ultipath is not None:
        shutil.copy2(i_dest_zip, ultipath)
        print 'the zipfile have been copy to the release folder'
    if deleteTemps(i_temp_folder):
        print 'work have been done'
    else:
        print 'delete folder failed'

if __name__=='__main__':
    print("begin to run")
    pyzipfiles()
    # i_test = '12345'
    # print  i_test.rfind('/')
