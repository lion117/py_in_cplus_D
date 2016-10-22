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
import PyZipper



g_sys_default_c='C:/Python27/lib/'
g_sys_default_d='D:/Python27/lib/'
g_sys_temp_dir = "C:/TempPyZip"
g_dest_zip= "D:/System/Desktop/python27.zip"

def sayhi():
    print "PycZipper begin to work"


######################################
#下面所有部分是相关的pyc抽取函数
#获得程序中所有模块的路径
def getPythonModulesPath():
    i_list = []
    #sys.modules是一个字典，数据格式如下：
    #{'site': <module 'site' from 'D:\Python27\lib\site.pyc'>,
    for itor in sys.modules.itervalues() :
        str_itor = str(itor)
        if "from" in str_itor:
            data = str_itor.split("'")
            i_list.append(data[-2])
        else :
            # print "module : ", s
            pass
    return i_list

#抽取文件
def extractFiles(t_dest_dir, t_src_list):
    t_dest_dir.replace("\\", "/")
    if t_dest_dir.rfind('\\') != 0 or t_dest_dir.rfind('/') != 0:
        t_dest_dir += '/'

    for itor in t_src_list :
        i_dest = pyPathFilter(t_dest_dir, itor)
        copyFiles(i_dest, itor)


def pyPathFilter(t_dest_dir, t_src_file):
    if len(t_src_file) ==0:
        raise ValueError("para could not be null")
        return
    t_src_file= t_src_file.replace("\\","/")
    i_lib_lenth = len(g_sys_default_c)

    if t_src_file.find(g_sys_default_c) != -1 or t_src_file.find(g_sys_default_d) != -1:
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
def copyFiles(t_dest_file, t_src_file):
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


def init():
    if os.path.exists(g_sys_temp_dir) is False :
        os.makedirs(g_sys_temp_dir)


def pyzipfiles():
    init()
    i_module_path = getPythonModulesPath()
    extractFiles(g_sys_temp_dir, i_module_path)
    # return
    # elimitcopy(g_sys_temp_dir)
    # argv = ("-c", g_dest_zip, "src", g_sys_temp_dir)
    # zipfile.main(argv)
    PyZipper.pyZipFile(g_sys_temp_dir, g_dest_zip)
    # cpy_py27dll()  # copy the python27.dll to the foledr
    # ultipath=find_targetfolder()
    # if ultipath is not None:
    #     shutil.copy2(g_dest_zip, ultipath)
    #     print 'the zipfile have been copy to the release folder'
    # if clean(g_sys_temp_dir):
    #     print 'work have been done'
    # else:
    #     print 'delete folder failed'


def generateZipPackage():
    argv = ("-c", g_dest_zip, "src", g_sys_temp_dir)
    zipfile.main(argv)
    cpy_py27dll()  # copy the python27.dll to the foledr
    ultipath = find_targetfolder()
    if ultipath is not None:
        shutil.copy2(g_dest_zip, ultipath)
        print 'the zipfile have been copy to the release folder'
    if deleteTemps(g_sys_temp_dir):
        print 'work have been done'
    else:
        print 'delete folder failed'


def simpleZip():
    i_list = getPythonModulesPath()
    for itor in i_list:
            print itor


if __name__=='__main__':
    print("begin to main")
    # pyzipfiles()
    # i_test = '12345'
    # print  i_test.rfind('/')
    # print os.getcwd()
    i_list = getPythonModulesPath()
    for itor in i_list:
        print itor


