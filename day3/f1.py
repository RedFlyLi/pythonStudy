#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ
'''
对请求参数做ascill码的排序
做url encode编码：name=。。。。
做MD5加密
'''

dict1= {"name":'sundy','age':18,'gender':'男','hobby':'同桌'}
#1
# dict1=dict(sorted(dict1.items(),key=lambda item:item[0]))
# print((dict1))
#2
from urllib import parse
# datas=parse.urlencode(dict1)
# print(datas)
#3
import hashlib
# md5=hashlib.md5()
# md5.update(datas.encode('utf-8'))
# print(md5.hexdigest())

def getMD5(**kwargs):
	dict1=dict(sorted(kwargs.items(),key=lambda item:item[0]))
	datas=parse.urlencode(dict1)
	md5 = hashlib.md5()
	md5.update(datas.encode('utf-8'))
	return md5.hexdigest()

print(getMD5(name='hxj',age='22',gender='nan',hobby='tongzuo'))