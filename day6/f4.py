#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import unittest
from selenium import webdriver

class BaiduTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Firefox()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get('http://www.baidu.com')

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
	'''百度首页链接测试'''
	def test_001(self):
		'''百度首页验证新闻'''
		self.driver.find_element_by_link_text('新闻').click()
		self.driver.back()

	def test_002(self):
		'''百度首页验证地图'''
		self.driver.find_element_by_partial_link_text('图').click()
		self.driver.back()

	# def test_003(self):
	# 	'''百度首页验证学术'''
	# 	self.driver.find_element_by_link_text('学术').click()
	# 	self.driver.back()

	'''百度首页搜索测试'''
	def test_003(self):
		'''百度首页搜索测试'''
		self.driver.find_element_by_id('kw').send_keys('webdriver')
		self.driver.back()

if __name__ == '__main__':
	suite=unittest.TestSuite()
	suite.addTest(BaiduTest('test_001'))
	suite.addTest(BaiduTest('test_002'))
	unittest.main(verbosity=2).run(suite)