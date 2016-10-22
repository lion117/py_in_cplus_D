#!/usr/bin/env python    
# -*- coding: utf-8 -*
# Created by Leo on 2016/10/15.

import sys, os

class ClassHandle:
    _var = 0
    def __init__(self, t_var):
        self._var=t_var

    def getVar(self):
        return self._var



if __name__ == "__main__":
    i_path = 'E:\\Git_demo\\py_in_cplus_D\\src\\PyConsole\\PyConsole/PyTemp/'
    # i_len = 0
    # if i_path.rfind("/") == 0 or i_path.rfind("\\") == 0:
    #     print "hellow"
    print  i_path.rfind("/")
    print  len(i_path)



    pass