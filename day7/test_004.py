#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import pytest

@pytest.mark.skip(reason='功能被取消')
def test_login_phone_001():
	assert 1==1

@pytest.mark.skip(reason='功能被取消')
def test_login_phone_002():
	assert 1==1

def test_login_email_001():
	assert 1==1

def test_login_email_002():
	assert 1==1