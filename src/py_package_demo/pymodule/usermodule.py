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
class userclass(object):
	def __init__(self,parent):
		print 'hi , userclass'

	def use_class_sayhi(self):
		print '=========================='
		print 'hi , this is user module is calling '
		print '=========================='


def use_module_sayhi():
	print '=========================='
	print 'hi , this is user module is calling '
	print '=========================='