#!/usr/bin/env python    
# -*- coding: utf-8 -*
# Created by Leo on 2016/10/22.

import sys, os
import threading
import time


g_obj = ScreenIO()

def getPyObj():
    return  g_obj

def regCallBackObj(t_obj):
    return  None





class ScreenIO(threading.Thread):
    def __init__(self):
        super(ScreenIO, self).__init__()
        self._is_stop = False
        self._callback_obj = None

    def onRecieve(self, t_data):
        import ScreenIO_py
        self._callback_obj.onRecieve(t_data)




    def run(self):
        print("_p begin to listen screen io....")
        while self._is_stop is False:
            i_data = raw_input()
            self.onRecieve(i_data)

    _is_stop = False
    _callback_obj = None

    def stop(self):
        self._is_stop = True

    def regCallback(self, t_obj):
        self._callback_obj = t_obj


    @staticmethod
    def main():
        i_this = ScreenIO()
        i_this.start()



if __name__ == "__main__":
    ScreenIO.main()

    pass