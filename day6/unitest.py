#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import unittest

class F1(unittest.TestCase):
	def setUp(self):
		print('我已经做好了准备工作')

	def tearDown(self):
		print('已处理')

	def test_001(self):
		admin
		print('adminn')

	def test_002(self):
		print('test2')

	def test_003(self):
		#print('test3')
		self.assertEqual(1,'1')

if __name__ == '__main__':
	unittest.main(verbosity=2)

'''
0代表得到执行的测试总数和全局结果
1代表得到成功的显示，失败的显示1，错误的显示0
2可以得到详细的信息
'''