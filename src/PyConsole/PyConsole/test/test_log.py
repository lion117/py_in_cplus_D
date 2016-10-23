#!/usr/bin/env python    
# -*- coding: utf-8 -*
# Created by Leo on 2016/10/16.

import sys, os
import  time
import test_interface

if __name__ == "__main__":
    i_ob = test_interface.getObjClass()
    print  i_ob.getCurrentTime()
    pass