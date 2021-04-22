#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import requests

# data={'mobileCode':'15828197200','userID':''}
# headers={'Content-Type':'application/x-www-form-urlencoded'}
# r=requests.post(
# 	url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo',data=data,headers=headers
# )
# print(r.text)

# data={'first':False,'pn':2,'kd':'测试架构师'}
# header={
#
# }
# params={ }
# r=requests.post(
# 	url=' ',data=data,headers=header,params=params
# )

r=requests.get('http://httpbin.org/get',timeout=60)
print(r.text)