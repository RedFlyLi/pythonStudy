#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import requests

class Method:
	def get(self,url,**kwargs):
		try:
			return requests.get(url=url, **kwargs)
		except BaseException as e:
			return e.args[0]

	def post(self,url,**kwargs):
		def get(self, url, **kwargs):
			try:
				return requests.post(url=url, **kwargs)
			except BaseException as e:
				return e.args[0]

obj=Method()
r=obj.post(url=url,headers=headers,data=data                                                                    )

r=obj.get(url='http://httpbin.org/get')
print(r.status_code)
print(r.text)