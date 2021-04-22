#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import unittest
from selenium import webdriver

class F3(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(100)
		self.driver.get('http://www.baidu.com')

	def tearDownClass(self):
		self.driver.quit()

	def test_baidu_news(self):
		self.driver.find_element_by_link_text('新闻').click()

	def test_baidu_map(self):
		self.driver.find_element_by_partial_link_text('图').click()

# class F1(unittest.TestCase):
# 	def setUp(self):
# 		print('我已经做好了准备工作')
#
# 	def tearDown(self):
# 		print('已处理')

	# def test_001(self):
	# 	admin
	# 	print('adminn')
	#
	# def test_002(self):
	# 	print('test2')
	#
	# def test_003(self):
	# 	#print('test3')
	# 	self.assertEqual(1,'1')

if __name__ == '__main__':
	unittest.main(verbosity=2)