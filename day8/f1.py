#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import requests

# r=requests.request(
# 	method='GET',
# 	url='http://httpbin.org/get')
# print(r.text)

# r=requests.get(url='http://httpbin.org/get')
# print(r.text)
# print('响应头',r.headers)
# print('json格式的数据：',r.json())
# print('基于文本的数据：',r.text)
# print('二进制的内容：',r.content)
# print('状态码：',r.status_code)
# print('cookies',r.cookies)

# r=requests.get('https://www.gushiwen.org/shiju/')
# print(r.text)

r=requests.post(url='http://httpbin.org/post')
print(r.text)
print(r.status_code)