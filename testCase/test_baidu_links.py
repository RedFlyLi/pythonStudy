#!/use/bin/env python
#coding:utf-8 

#Author:HXJ


from selenium import  webdriver
import  unittest

class BaiudLink(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://www.baidu.com')


	def tearDown(self):
		self.driver.quit()

	def test_001(self):
		self.driver.find_element_by_link_text('新闻').click()
		#self.assertEqual(self.driver.current_url,'http://news.baidu.com/')
		self.driver.back()

	def test_002(self):
		self.driver.find_element_by_partial_link_text('图').click()
		#self.assertEqual(self.driver.current_url,'https://map.baidu.com/')
		self.driver.back()

if __name__ == '__main__':
    unittest.main(verbosity=2)