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
    i_this = ClassHandle(20)
    print i_this.getVar()
    print ClassHandle._var


    pass