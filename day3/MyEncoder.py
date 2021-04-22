#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import json
class MyEncoder(json.JSONEncoder):
	def default(self, obj):

		if isinstance(obj,bytes):
			return str(obj,encoding='utf-8')

		return json.JSONEncoder.default(self,obj)