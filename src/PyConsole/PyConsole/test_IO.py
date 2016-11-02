#!/usr/bin/env python    
# -*- coding: utf-8 -*
# Created by Leo on 2016/11/1.

import  os,time
import  threading

def getPyObj():
    return  ScreenIO()

class ScreenIO(threading.Thread):
    _cplus_obj = None
    def __init__(self):
        self._cplus_obj = None
        threading.Thread.__init__(self)

    def regFuc(self,t_obj):
        import ScreenIO_py
        self._cplus_obj = t_obj
        t_obj.onRecieve("py regist")



    def run(self):
        while True:
            i_data = raw_input()
            self.onRecive(i_data)


    def onRecive(self,t_str):
        print ("Py: "+ t_str)
        import ScreenIO_py
        self._cplus_obj.onRecieve(t_str)






if __name__ == "__main__":
    i_this = ScreenIO()
    i_this.start()



    pass