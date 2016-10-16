#!/usr/bin/env python    
# -*- coding: utf-8 -*
# Created by Leo on 2016/10/16.

import sys, os

import logging
import logging.config

import logging
import logging.config


logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


if __name__ == "__main__":
    logging.debug('This is debug message')
    logging.info('This is info message')
    logging.warning('This is warning message')
    logging.error('This is error message')
    logging.fatal('This is fatal message')


    pass