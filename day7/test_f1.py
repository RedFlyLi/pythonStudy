#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import pytest
import unittest

def test_001():
	assert 1==1

class Testlogin(object):
	def test_login(self):
		assert  1==1

class loginTest(unittest.TestCase):
	def test_login_001(self):
		pass

def add(a,b):
	return a+b

def test_add():
	try:

		assert add(1,'1')==2
	except Exception as e:
		print(e.args[0])