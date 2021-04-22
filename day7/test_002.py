#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import pytest

@pytest.mark.smoke
def test_smoke_001():
	assert 1==1

@pytest.mark.smoke
def test_smoke_002():
	assert 1==1

@pytest.mark.login
def test_login_001():
	assert 1==1

@pytest.mark.lgout
def test_lgout_001():
	assert 1==1

def test_002():
	assert 1==2