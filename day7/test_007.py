#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import pytest
import requests

@pytest.fixture()
def data():
	return 'hello'

def test_data(data):
	assert data=='hello'

@pytest.fixture()
def getToken():
	'''获取token'''
	r=requests.post(
		url='http://cdqserver.cn:5001/loginUser',
		json={
    "loginUser": {
        "account": "cdq",
        "pass": "111111",
        "role": "student"
    }
})
	return r.json()['token']
	print(r.json())

def test_get_allMessage(getToken):
	pass

if __name__=='main':
	pytest.main(["-v","-s","test_007.py"])
