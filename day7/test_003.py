#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import requests
import pytest

def test_baidu():
	r=requests.get(url='http://www.baidu.com/')
	assert r.status_code==200

def test_taobao():
	r = requests.get(url='http://www.taobao.com/')
	assert r.status_code == 200

def test_jd():
	r = requests.get(url='http://www.jd.com/')
	assert r.status_code == 200

def test_sina():
	r = requests.get(url='http://www.sina.com/')
	assert r.status_code == 200
