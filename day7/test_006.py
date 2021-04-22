#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import yaml

def readYaml():
	with open('login.yaml','r',encoding='utf-8') as f:
		return list(yaml.safe_load_all(f))

#print(readYaml())
for item in readYaml():
	print(item)