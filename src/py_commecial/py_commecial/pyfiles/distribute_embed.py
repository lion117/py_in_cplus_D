# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 20:26:09 2014

@author: LEO
"""
import sys
import os
import shutil


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



def test():
    a = getModulesPath()
    extractFiles("testpg\\", a) #抽取后的文件会放到testpg目录下

if __name__=="__main__":
    module=getModulesPath()
    for i in module:
        print i