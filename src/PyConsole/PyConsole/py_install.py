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
    print "===================="
    print "hello , this is python speaking "
    print '===================='

######################################
#下面所有部分是相关的pyc抽取函数
#获得程序中所有模块的路径
def getModulesPath():
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
def extractFiles(destDir, files):
    destDir.replace("/", "\\")
    if destDir[-1] != '\\' :
        destDir += '\\'

    for f in files :
        dest = filiterPath(destDir, f)
        copyF(dest, f)

#过滤路径 去掉最大绝对路径
def filiterPath(destDir, srcFile):
    dest = destDir
    maxLen = 0
    for path in sys.path:
        lenp = len(path)
        if lenp < len(srcFile) and path == srcFile[:lenp]:
            if maxLen < lenp:
                dest = destDir + srcFile[lenp+1:]
                maxLen = lenp

    dest.replace("/", "\\")
    if '.' in dest: #去掉文件名
        p = dest.rfind('\\')
        if p >= 0:
            dest = dest[:p]
    return dest

#拷贝文件
#如果目标路径不存在，则创建
def copyF(destDir, srcFile):
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

# delete .py resouce files , make sure all files is pyc compile files
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



def test():
    a = getModulesPath()
    DEST_ZIP_FILE="D:\System\Desktop/python27.zip"
    DEST_PATH="D:\System\Desktop/test"
    extractFiles(DEST_PATH, a)

    elimitcopy(DEST_PATH)
    argv = ("-c", DEST_ZIP_FILE, "src", DEST_PATH)
    zipfile.main(argv)

    if deltempdir(DEST_PATH):
        print 'work have been done'
    else:
        print 'delete folder failed'

if __name__=='__main__':
    test()