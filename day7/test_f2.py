#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import pytest
from selenium import webdriver

# @pytest.fixture()
# def init():
# 	print('初始化')
# 	yield
# 	print('清理')
#
# def test_one(init):
# 	print('测试步骤：')

import requests

def test_taobao():
	r=requests.get(url='http://www.baidu.com')
	print('taobao:\n',r.elapsed.total_seconds())