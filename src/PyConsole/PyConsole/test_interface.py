#!/usr/bin/env python
# -*- coding: utf-8 -*
# Created by Leo on 2016/10/16.
import os
import time

def add(t_a, t_b):
    return t_a + t_b


def getCurrentDir():
    return os.getcwd()


def getWorkingDir():
    return os.path.dirname(os.getcwd()) + "/Bin"


class TestClass():
    _name = "default"

    def __init__(self, t_name):
        self._name = t_name

    def add(self, t_a, t_b):
        return t_a + t_b

    def getCurrentTime(self):
        return str(time.ctime())

    def whoAmI(self):
        print self._name


def getObjClass():
    return TestClass("t_name")


