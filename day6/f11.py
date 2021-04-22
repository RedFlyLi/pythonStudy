#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

from day6.init import *

class BaiduLink(Init):
	# def test_baidu_news(self):
	# 	print(self.driver.title)
	# 	self.assertEqual(self.driver.title,'百度一下，你就知道')

	# def test_baidu_login(self):
	# 	so=self.driver.find_element_by_id('kw')
	# 	print(so.is_enabled())
	# 	self.assertTrue(so.is_enabled())

	def test_baidu_title(self):
		self.assertIn('百度',self.driver.title)

if __name__ == '__main__':
	unittest.main(verbosity=2)