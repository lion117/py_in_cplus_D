# -*- coding: utf-8 -*-
"""
Created on 2014/8/21
@author: LEO
"""


from zipfile import *
import zipfile
import  os ,sys


def pyZipFile(t_src, t_dest):
    if os.path.isdir(t_src)  is False:
        print  u'无效的文件夹路径' , t_src
        raise  ValueError
        return False

    if t_dest is None:
        t_dest =os.path.join(os.getcwd() , 'default.zip')

    if len(t_dest) is 0:    # take use the defaut path
        t_dest=os.path.join(os.getcwd() , 'default.zip')

    if os.path.exists(t_dest):
        os.remove(t_dest)

    fzip = zipfile.ZipFile(t_dest, 'w', zipfile.ZIP_DEFLATED)
    i_basename = os.path.basename(t_dest)

    for dirpath,dirfilename, filenames in os.walk(t_src,False):
        for filename in filenames:
            if '.idea' in dirpath:
                break
            if i_basename == filename:
                print("target zip file had been skipped")
                break
            item_file =filename
            if dirpath != t_src:
                item_file =  dirpath[len(t_src)+1:] + '/' + filename
            i_file = os.path.join(dirpath, filename)
            try:
                fzip.write(i_file,item_file)
            except RuntimeError ,ex:
                print(ex)
                fzip.close()
                return False

    fzip.close()
    return  True




def walkPath(t_path):
    print  t_path
    for (dirpath, dirnames, filenames) in os.walk(t_path):
        for filename in filenames:
            if '.idea' in dirpath:
                break
            if dirpath == t_path:
                print(os.path.join(dirpath, filename))  + "   "+ filename
            else:
                ext_folder = dirpath[len(t_path):]+ '/'
                print(os.path.join(dirpath, filename))  + "   "+ ext_folder+filename

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print  u"错误：请指定需要压缩的文件夹路径"
    else:
        i_path = sys.argv[0]
        i_src = sys.argv[1]
        i_dest =''
        if len(sys.argv) == 2:
            i_dest = None
        else:
            i_dest = sys.argv[2]
        pyZipFile(i_src, i_dest)
    # walkPath(os.getcwd())


