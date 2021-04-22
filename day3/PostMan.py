#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import json
import requests

def readJson():
	return json.load(open('x.login','r',encoding='UTF-8'))

# print(readJson())
# def one_get():
# 	r=requests.request(
# 		method=readJson()['item'][0]['request']['method'],
# 		url=readJson()['item'][0]['request']['url']['raw'])
# 	print(r.login())

#print(type(readJson()))
#one_get()

def one_get1():
	for item in readJson()['item']:
		# print(item['request']['method'])
		if item['request']['method']=='GET':
			r = requests.request(
				method=item['request']['method'],
				url=item['request']['url']['raw'])
			print(r.json())
		elif item['request']['method'] == 'POST':
			r = requests.request(
				method=item['request']['method'],
				url=item['request']['url']['raw'],
				#login=login.loads(item['request']['body']['raw'])
			)
			print(r.json())

one_get1()




