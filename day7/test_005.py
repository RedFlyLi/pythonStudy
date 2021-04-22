#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import pytest

def add(a,b):
	return a+b

'''
是对列表中的对象循环，然后一一的赋值
对象：
列表：
元组：
字典
'''

@pytest.mark.parametrize('a,b,expect',[
	[1,1,2],
	[2,2,4],
])
def test_add(a,b,expect):
	assert add(a,b)==expect

if __name__ == '__main__':
	pytest.main(["-s","-v","test_005.py"])